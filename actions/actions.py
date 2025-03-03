import csv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet 

class ActionCheckRegionMembers(Action):
    def name(self) -> Text:
        return "action_check_region_members"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        region = tracker.get_slot("region")
        members_exist = False

        with open("data/community_members.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Region'].strip().lower() == region.strip().lower():
                    members_exist = True
                    break

        response = f"Yes, there are members in {region}." if members_exist else f"No, there are no members in {region}."
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

        with open("data/community_members.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Region'].strip().lower() == region.strip().lower():
                    names.append(row['Name'])

        if names:
            response = f"The members in {region} are: {', '.join(names)}."
        else:
            response = f"No members found in {region}."
        dispatcher.utter_message(text=response)
        return []

class ActionProvideMemberDetails(Action):
    def name(self) -> Text:
        return "action_provide_member_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")

        print(f"DEBUG: Extracted name slot value -> {name}")  # 🚀 Debugging

        if not name:
            dispatcher.utter_message(text="❌ No name provided. Please specify a member.")
            return [SlotSet("name", None)]  # Reset slot

        name = str(name).strip().lower()
        member_found = False

        with open("data/community_members.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if str(row['Name']).strip().lower() == name:
                    member_found = True
                    response = f"📌 Details for {row['Name']}: \n📧 Email: {row['Email']}, ☎️ Phone: {row['Phone']}"
                    break

        if not member_found:
            response = f"❌ No details found for {name.title()}."

        dispatcher.utter_message(text=response)
        return [SlotSet("name", None)]  # ✅ Reset slot after responding
