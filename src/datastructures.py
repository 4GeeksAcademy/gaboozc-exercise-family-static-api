
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name: str, initial_members: list = []):
        self.last_name = last_name
        self._members = []

        for member in initial_members:
            self.add_member(member)

    # Add a new member to the family
    def add_member(self, member):
        self._members.append(member)

    # Delete a member from the family by ID
    def delete_member(self, id):
        self._members = [member for member in self._members if member["id"] != id]

    # Get a specific member by ID
    def get_member(self, id: int):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # Get all members of the family
    def get_all_members(self):
        return self._members