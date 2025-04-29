#Bearcat Bistro Ordering System

**Data Structure Choices**

_Menu:_ I chose to use an array for the menu, since I decided to access the drinks by assigning each a number. The indexing system of an array made the numbering simpler, and the time complexity for accessing an item in this fashion was constant. I also included an option for accessing the drinks by name which could have been made simpler by using a datastructure like a dictionary, and using drink names as keys. This was a tradeoff of using the array. 

_Customer Order/Order Confiramtion:_ I stored the customer order in a specific object designed for it, including a string for the name and a linked list to hold the drink objects associated with the order. This class was designed to print out for order confirmation as well, making use of the same data reference. This object provided a flexibility that was useful in adding to and removing from the order, simplifying memory useage when frequently expanding and contracting the linked list. On the few occasions where an object has to be located in the list, this process has time complexity O(n) as the linked list requires iteration. This is a trade off of the strucutre, however as the use of the linked list is to hold drink orders, it is unlikely it will grow very large, as bulk drink orders are not common at cafes. Many instances of accessing items in this list, also require iteration through it, as all the items are being printed out. 

_Open Orders:_ I used a Deque to store the open orders. It makes sense to use a data structure which can imitate a queue for orders which will be put in a line to be completed one at a time, and finished in the order they are submitted, according to the first in, first out pattern. The Deque has the advantage of being able to cancel or edit orders after they have been added to the queue. This structure allows for constant time complexity access to its head and tail, the elements which will matter the most in this situation. In a real world bistro situation, drinks can be finished slightly out of order if different baristas are making them, which poses an issue with this implementation as only the first drink in line can be marked as complete. In an ideal situation however, it works well. 

_Completed Orders:_ The completed order structure was implemented as a bag of the drinks from each order. This served for simple calculations on the end of day report, as the numbers of each drink sold were already tallied, and the information of which customers ordered what was no longer needed. Though the time complexity to get the number of each drink sold is O(n), the n represents the generic drink types that have been ordered from the menu, not every single drink ordered in the day. For this reason, using this structure greatly simplifies the process. If, for future reference, the additional information from each order was needed (such as name of customer), this system would fail, and another data structure would be needed to hold the individual orders. 





**Sample Output**

![alt text](output_imgs/image.png)
![alt text](output_imgs/image-1.png)
![alt text](output_imgs/image-2.png)
![alt text](output_imgs/image-3.png)




**Limitations/ Next Steps**
There are currently no known bugs in my code, there are several limitations however. When editing an order, the user can't add to the order without removing a drink. Also, when the user removes a drink, it simply takes the first drink with the given name. With more time, I would like to restructure the order editing function to have more functionality such as being able to change customization, choose to remove specific drinks of a type, and maneuver in and out of editing more easily. 

In general, the exiting processes could be more specific and easy to use. I would like to improve the visual layout, and implement some of the extensions such as saving daily reports and creating accounts, as well. 