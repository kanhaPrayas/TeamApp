# Constants file for any constants getting used accross project

# ApiCore app Constants

# models.py
ROLE_CHOICES = (
    ("admin", "admin",),
    ("regular", "regular"),
)
DELETED_STATUS = -1

# views.py
NO_MEMBER_ERROR = {"message": "No such member exists"}
INVALID_INPUT_JSON = {"message": "Invalid data content"}

VALID_TELEPHONE_STRING = """
							(+91)8884599393,
							+918884599393,
							8884599393,
							(+1)123-456-7890,
							(+1)123.456.7890
						"""
