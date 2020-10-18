from django.test import TestCase
from maniva_webapp.models import Contact


class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(
            name="Jane Doe",
            email="janed@gmail.com",
            subject="bioinformatics",
            message="Does your consulting into the biomedical sciences?",
        )
        Contact.objects.create(
            name="John Doe",
            email="johnd@outlook.com",
            subject="consulting trials",
            message="Do you have trial periods for consulting?",
        )

    def test_contact_forms(self):
        """properly connected contact forms"""
        contact1 = Contact.objects.get(name="Jane Doe")
        contact2 = Contact.objects.get(name="John Doe")
        self.assertEqual(contact1.message)