from ultralytics import YOLO
import cv2
from tkinter import *
from threading import Thread
import pymysql




def check(object_coordinates, midpoint):

    x1 = object_coordinates[0] # x1 is the top left x-coordinate of the object detected

    if x1 >= midpoint:
          return True
    
    return False





def start_tkinter():
    global window, stock_entry, cart_entry
    window = Tk()

    Label(window, text = "Stock").pack()
    stock_entry = Entry(window)
    stock_entry.pack()

    Label(window, text = "Cart").pack()
    cart_entry = Entry(window)
    cart_entry.pack()

    window.mainloop()



def execute_query(query):
     cursor.execute(query)
     conn.commit()


def main():
    global number_of_objects_in_cart, number_of_objects_in_stock, conn, cursor

    conn = pymysql.connect(host="Localhost", user="root", password="", database="hackathon_db")
    cursor = conn.cursor()

    execute_query("delete from stock")
    execute_query("delete from cart")

    

    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)


    object_ids = [39]
    object_names = ['Water Bottle']

    for i in range(len(object_ids)):
         execute_query("insert into stock values (%s, '%s', %s)" % (object_ids[i], object_names[i], 0))
         execute_query("insert into cart values (%s, '%s', %s)" % (object_ids[i], object_names[i], 0))

    created_tkinter = False

    while True:
            
            number_of_objects_in_stock = 0
            number_of_objects_in_cart = 0

            if not created_tkinter:
                Thread(target = start_tkinter).start()
                created_tkinter = True

            _, frame = cap.read()

            height, width = frame.shape[0], frame.shape[1]

            midpoint = width // 2
            start = (midpoint, 0)
            end = (midpoint, height)

            cv2.line(frame, start, end, (0, 0, 255), 2)

            objects_detected = model(frame)[0].boxes.data.tolist()

            execute_query("update cart set object_quantity = 0")
            execute_query("update stock set object_quantity = 0")

            for object in objects_detected:
                
                object_id = object[-1]

                if object_id in object_ids:

                    object_coordinates = [object[i] for i in range(4)]

                    object_name = object_names[object_ids.index(object_id)]
                
                    purchased = check(object_coordinates, midpoint)

                    if purchased:
                        cursor.execute("select object_quantity from cart where object_id = %s" % object_id)
                        current_quantity = cursor.fetchone()[0]
                        number_of_objects_in_cart = current_quantity + 1

                        # Draw bounding boxes and labels on the frame
                        cv2.rectangle(frame, (int(object[0]), int(object[1])), (int(object[2]), int(object[3])), (0, 255, 0), 2)
                        cv2.putText(frame, object_names[object_ids.index(int(object[-1]))] + " PURCHASED", (int(object[0]), int(object[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                        
                        execute_query("update cart set object_quantity = %s where object_id = %s" % (number_of_objects_in_cart, object_id))
                    else:
                        cursor.execute("select object_quantity from stock where object_id = %s" % object_id)
                        current_quantity = cursor.fetchone()[0]
                        number_of_objects_in_stock = current_quantity + 1

                        # Draw bounding boxes and labels on the frame
                        cv2.rectangle(frame, (int(object[0]), int(object[1])), (int(object[2]), int(object[3])), (0, 255, 0), 2)
                        cv2.putText(frame, object_names[object_ids.index(int(object[-1]))] + " IN STOCK", (int(object[0]), int(object[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                        
                        execute_query("update stock set object_quantity = %s where object_id = %s" % (number_of_objects_in_stock, object_id))
            
            stock_entry.delete(0, END)
            stock_entry.insert(0, number_of_objects_in_stock)

            cart_entry.delete(0, END)
            cart_entry.insert(0, number_of_objects_in_cart)


            cv2.imshow("Object Tracking", frame)

            if cv2.waitKey(30) == 27:
                break
    
    conn.close()


main()