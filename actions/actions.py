import csv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckRegionMembers(Action):
    def name(self) -> Text:
        return "action_check_region_members"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        region = tracker.get_slot("region")
        members_exist = False

        with open("data/community_members.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Region'].lower() == region.lower():
                    members_exist = True
                    break

        response = "Yes, there are members in {}.".format(region) if members_exist else "No, there are no members in {}.".format(region)
        dispatcher.utter_message(text=response)
        return []

class ActionListMembers(Action):
    def name(self) -> Text:
        return "action_list_members"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        region = tracker.get_slot("region")
        names = []

        with open("data/community_members.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Region'].lower() == region.lower():
                    names.append(row['Name'])

        if names:
            response = "The members in {} are: {}.".format(region, ', '.join(names))
        else:
            response = "No members found in {}.".format(region)
        dispatcher.utter_message(text=response)
        return []

class ActionProvideMemberDetails(Action):
    def name(self) -> Text:
        return "action_provide_member_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        member_found = False

        with open("data/community_members.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Name'].lower() == name.lower():
                    member_found = True
                    response = f"Details for {name}: Email: {row['Email']}, Phone: {row['Phone']}"
                    break

        if not member_found:
            response = f"No details found for {name}."
        dispatcher.utter_message(text=response)
        return []