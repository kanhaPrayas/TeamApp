# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


class ModelTestCase(TestCase):
    """This class defines the test suite for the team model."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.dummy_first_name = "DummyFN"
        self.dummy_last_name = "DummyLN"
        self.dummy_age = 27
        self.dummy_role = "admin"
        self.dummy_phone = "(+91)8884599393"
        self.dummy_email = "dummy@dummy.com"
        self.dummy_status = 0

        self.dummy_team = Team(first_name=self.dummy_first_name,
                               last_name=self.dummy_last_name,
                               age=self.dummy_age,
                               role=self.dummy_role,
                               phone=self.dummy_phone,
                               email=self.dummy_email,
                               status=dummy_status
                               )

    def test_model_can_create_a_team_member(self):
        """Test the Team model can create a team member."""

        old_count = Team.objects.count()
        self.dummy_team.save()

        new_count = Team.objects.count()
        self.assertNotEqual(old_count, new_count)
