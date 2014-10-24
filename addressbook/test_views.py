# coding=utf-8
from django.test import TestCase

from django.core.urlresolvers import reverse
import mock

from addressbook.models import School


__author__ = 'edwardotis'


def create_and_save_school(name, zipcode, email=''):
    """
    Creates a school with given fields and saves it to the db
    """
    return School.objects.create(name=name, zipcode=zipcode, email=email)


def create_school(name, zipcode, email, school_id):
    '''
    Return transient school object
    :param name:
    :param zipcode:
    :param email:
    :return:
    '''
    return School(name=name, zipcode=zipcode, email=email, school_id=school_id)

class AddressbookViewTests(TestCase):
    def test_school_detail(self):
        """
        Basic test of school detail end to end
        """

        # GIVEN
        expectedName = 'MIT'
        expectedZip = 10000
        expectedEmail = 'fake@localhost.com'
        expectedSchool = create_and_save_school(expectedName, expectedZip, expectedEmail)

        # WHEN
        response = self.client.get(reverse('addressbook:school_detail', args=(expectedSchool.school_id,)))

        # THEN
        actualSchool = response.context['school']
        self.assertEquals(actualSchool.name, expectedName)
        self.assertEquals(actualSchool.zipcode, expectedZip)
        self.assertEquals(actualSchool.email, expectedEmail)

    def test_create_school(self):
        # given
        expectedName = 'MIT'
        expectedZip = 10000
        expectedEmail = 'fake@localhost.com'
        post_data = {'email': expectedEmail,
                     'name': expectedName,
                     'zipcode': expectedZip,
        }

        # when
        response = self.client.post(reverse('addressbook:create_school'), post_data)

        #then
        #assert redirect url
        self.assertEquals(response.url, 'http://testserver/addressbook/school/1/')

        #assert db creation of school with post params
        actualSchool = School.objects.filter(name=expectedName)[0]
        self.assertEquals(actualSchool.name, expectedName)
        self.assertEquals(actualSchool.zipcode, expectedZip)
        self.assertEquals(actualSchool.email, expectedEmail)

    def test_delete_school(self):
        # GIVEN
        expectedName = 'MIT'
        expectedZip = 10000
        expectedEmail = 'fake@localhost.com'

        expectedSchool = create_and_save_school(expectedName, expectedZip, expectedEmail)
        expectedSchoolId = expectedSchool.school_id
        self.assertTrue(School.objects.filter(school_id=expectedSchoolId).exists())

        # WHEN
        response = self.client.post(reverse('addressbook:delete_school', args=(expectedSchool.school_id,)))

        # THEN
        # assert correct redirect url
        self.assertEquals(response.url, 'http://testserver/addressbook/school/')

        #assert db creation of school with post params
        self.assertFalse(School.objects.filter(school_id=expectedSchoolId).exists())

    def test_update_school(self):
        # GIVEN
        expectedName = 'MIT'
        expectedZip = 10000
        expectedEmail = 'fake@localhost.com'
        expectedSchool = create_and_save_school(expectedName, expectedZip, expectedEmail)
        expectedSchoolId = expectedSchool.school_id

        # assert old values
        actualSchool = School.objects.get(school_id=expectedSchoolId)
        self.assertEquals(actualSchool.name, expectedName)
        self.assertEquals(actualSchool.zipcode, expectedZip)
        self.assertEquals(actualSchool.email, expectedEmail)

        #prepare update values
        expectedName = 'Stanford'
        expectedZip = 9
        expectedEmail = 'newfake@localhost.com'

        updated_post_data = {'email': expectedEmail,
                             'name': expectedName,
                             'zipcode': expectedZip,
        }


        # WHEN
        response = self.client.post(reverse('addressbook:update_school', args=(expectedSchool.school_id,)),
                                    data=updated_post_data)

        # THEN
        # assert correct redirect url
        self.assertEquals(response.url, ('http://testserver/addressbook/school/%s/' % expectedSchoolId))

        #assert newly updated values in db.
        actualSchool = School.objects.get(school_id=expectedSchoolId)
        self.assertEquals(actualSchool.name, expectedName)
        self.assertEquals(actualSchool.zipcode, expectedZip)
        self.assertEquals(actualSchool.email, expectedEmail)

    def test_list_schools(self):
        '''
        :return:
        '''

        # GIVEN
        expectedName = 'MIT'
        expectedZip = 10000
        expectedEmail = 'fake@localhost.com'
        expectedSchool = create_and_save_school(expectedName, expectedZip, expectedEmail)
        expectedSchoolId = expectedSchool.school_id

        expectedName2 = 'Stanford'
        expectedZip2 = 9
        expectedEmail2 = 'newfake@localhost.com'
        expectedSchool2 = create_and_save_school(expectedName2, expectedZip2, expectedEmail2)
        expectedSchoolId2 = expectedSchool2.school_id

        # WHEN
        response = self.client.get(reverse('addressbook:school_list'), data={'sort_by': '-name'})

        # THEN
        actualSchools = response.context['schools_list']
        self.assertEqual(len(actualSchools), 2)

        # descending name sort

        #stanford
        self.assertEquals(actualSchools[0].school_id, expectedSchoolId2)
        self.assertEquals(actualSchools[0].name, expectedName2)
        self.assertEquals(actualSchools[0].zipcode, expectedZip2)
        self.assertEquals(actualSchools[0].email, expectedEmail2)

        # mit
        self.assertEquals(actualSchools[1].school_id, expectedSchoolId)
        self.assertEquals(actualSchools[1].name, expectedName)
        self.assertEquals(actualSchools[1].zipcode, expectedZip)
        self.assertEquals(actualSchools[1].email, expectedEmail)

    @mock.patch('addressbook.views.school_service')
    def test_list_schools_mocked(self, mock_school_svc):
        '''
        Test without hitting a real backing database
        :return:
        '''

        # GIVEN
        expectedName = 'MIT'
        expectedZip = 10000
        expectedEmail = 'fake@localhost.com'
        expectedSchoolId = 5
        expectedSchool = create_school(expectedName, expectedZip, expectedEmail, expectedSchoolId)

        expectedName2 = 'Stanford'
        expectedZip2 = 9
        expectedEmail2 = 'newfake@localhost.com'
        expectedSchoolId2 = 42
        expectedSchool2 = create_school(expectedName2, expectedZip2, expectedEmail2, expectedSchoolId2)

        expected_data = {'schools_list': [expectedSchool2, expectedSchool]}

        # setup mock method to avoid db call
        mock_school_svc.get_schools_list = mock.Mock(return_value=expected_data)

        # WHEN
        response = self.client.get(reverse('addressbook:school_list'), data={'sort_by': '-name'})

        # THEN
        actualSchools = response.context['schools_list']
        self.assertEqual(len(actualSchools), 2)

        # descending name sort

        # stanford
        self.assertEquals(actualSchools[0].school_id, expectedSchoolId2)
        self.assertEquals(actualSchools[0].name, expectedName2)
        self.assertEquals(actualSchools[0].zipcode, expectedZip2)
        self.assertEquals(actualSchools[0].email, expectedEmail2)

        # mit
        self.assertEquals(actualSchools[1].school_id, expectedSchoolId)
        self.assertEquals(actualSchools[1].name, expectedName)
        self.assertEquals(actualSchools[1].zipcode, expectedZip)
        self.assertEquals(actualSchools[1].email, expectedEmail)

        #assert mock method was called with expected parameters
        mock_school_svc.get_schools_list.assert_called_once_with('-name')
