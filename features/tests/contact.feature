# Created by Ryan at 6/17/2026
Feature: Contact Us
"""
1- Open the main page https://soft.reelly.io
2- Log in to the page.
3- Click on the settings option.
4- Click on the Contact us option.
5- Verify the right page opens.
6- Verify the WhatsApp button is clickable.
"""
  Scenario: User can contact via WhatsApp
    Given Open Reelly main page
    Then User can log in
    Then User can navigate to settings
    Then User can click contact us
    When User is on the contact-us page
    Then WhatsApp button is clickable