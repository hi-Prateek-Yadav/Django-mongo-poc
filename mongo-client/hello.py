# db.createCollection(
#   "contact",
#   {
#   "validator": {
#     "$jsonSchema": {
#       "bsonType": "object",
#       "title": "Contact Object Validation",
#       "required": ["_id", "name", "phone_number", "age"],
#       "properties": {
#         "_id": {
#           "bsonType": "string",
#           "description": "'Id' is required"
#         },
#         "name": {
#           "bsonType": "string",
#           "description": "'Name' must be a string and is required"
#         },
#         "phone_number":{
#           "bsonType":"string",
#           "description":"'Phone Number' must be a string and is required"
#         },
#         "age":{
#           "bsonType":"int",
#           "minimum":0,
#           "maximum":150,
#           "description":"'Age' must be an integer and between 0-150"
#         }
#       }
#     }
#   },
#   "validationLevel":"strict",
#   "validationAction":"error"
# })