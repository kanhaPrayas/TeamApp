#Constants file for any constants getting used accross project

#ApiCore app Constants

#models.py
ROLE_CHOICES = (
				("admin","admin",),
				("regular","regular"),
				)
DELETED_STATUS = -1

#views.py
NO_MEMBER_ERROR = "No such member exists"
INVALID_INPUT = "Invalid data content"