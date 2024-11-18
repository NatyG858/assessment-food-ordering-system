''' JavaScript Object Notation '''
import json

menu_string = '''
 {
	"Food": [
		{
	       "name": " Burger " ,
		   "price": "10"
		},
		{   
			"name": "Pizza" ,
		    "price": "20"
		},
		{  
			"name": "Sandwich" ,
			"price": 18
		}

		],


    "Drinks": [

		{
	       "name": "Coca-Cola" ,
		   "price": "6"
		},
		{   
			"name": "Pepsi" ,
		    "price": "7"
		},
		{  
			"name": "Fruit tea" ,
			"price": "3"
		}

		],


    "Desserts": [ 

		{
	       "name": "Cheesecake" ,
		   "price": "10"
		},
		{   
			"name": "Ice Cream" ,
		    "price": "7"
		},
		{  
			"name": "Lemon Pie"  ,
			"price": "3"
		}

		]
}
'''
data = json.loads(menu_string)
print(data)