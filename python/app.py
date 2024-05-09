import random
from humaserverplatform import Plugin, Widget

class MedicationTrackerWidget: Widget
    name = "MedicationTracker"
    _id = "com.huma.medicationtracker"
    

plugin = Plugin("MedicationTracker")
widget = MedicationTrackerWidget("MedicaitonTracker")
plugin.add(widget)

@widget.function("search")
def search():
    return random.choice(["Penicillin", "Aspirin", "Insulin", "Morphine", "Ibuprofen (Advil, Motrin)"])
