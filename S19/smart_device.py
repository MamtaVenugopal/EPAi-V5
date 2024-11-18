from typeguard import typechecked

@typechecked
class SmartDevice:
  device_count = 0  # Overall device count
  category_counts = {  # Counts for each category
        "cat_1": 0,
        "cat_2": 0,
        "cat_3": 0,
        "cat_4": 0,
        "cat_5": 0,
        "cat_6": 0,
     }
  created_devices = set()
  cat_1 = {'Thermostat', 'Heater', 'Microwave', 'Oven'}  # heating smart devices
  cat_2 = {'Fan'}  # cooling smart devices
  cat_3 = {'Light', 'Lamp'}  # lighting smart devices
  cat_4 = {'Doorbell', 'Lock'}  # door smart devices
  cat_5 = {'Speaker', 'Camera', 'Router'}  # phone or computer smart devices
  cat_6 = {'Vacuum'}

  def __init__(self, device_name: str, model_number: str, is_online: bool = False, status: dict = None):
        # Check categories and increment counts
        categories = [SmartDevice.cat_1, SmartDevice.cat_2, SmartDevice.cat_3, SmartDevice.cat_4, SmartDevice.cat_5, SmartDevice.cat_6]
        category_names = ["cat_1", "cat_2", "cat_3", "cat_4", "cat_5", "cat_6"]

        for i, category in enumerate(categories):
            if device_name in category:
                SmartDevice.category_counts[category_names[i]] += 1  # Increment category count
                if SmartDevice.category_counts[category_names[i]] == 1:
                   SmartDevice.device_count += 1 
                break  # Stop checking after finding the category

        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = status if status is not None else {}

  def update_status(self,attribute,value):
    """Adds or updates a status attribute in the status dictionary."""
    self.status[attribute] = value
    
  def get_status(self,attribute):
    """Returns the value of a specific status attribute.
    If the attribute does not exist' it should return 'Attribute not found'.
    """
    return self.status.get(attribute, "Attribute not found")
  def toggle_online(self):
    """Toggles the is_online attribute between True and False."""
    self.is_online = not self.is_online

  def reset(self):
        """Resets all status attributes to their default values
        (i.e., clears the status dictionary).
        """
        self.status = {}  # Assign an empty dictionary to status

  def __call__(self):
        """Makes the SmartDevice class callable.

        Returns:
            str: A formatted string containing the device_name and model_number.
        """
        return f"{self.device_name} (Model: {self.model_number})"

  def device_info(self):
        """Returns the current state of the device as a dictionary."""
        return {
            "device_name": self.device_name,
            "model_number": self.model_number,
            "is_online": self.is_online,
            "status": self.status,
        }