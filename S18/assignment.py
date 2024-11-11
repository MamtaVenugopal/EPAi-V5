
import json
from datetime import date, datetime
from decimal import Decimal
from marshmallow import Schema, fields, post_load # Import post_load from marshmallow


class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
    def __repr__(self):
        #formatted_date = self.date.strftime('%Y, %m, %d')
        return f"Stock('{self.symbol}', Date({self.date.strftime('%Y, %m, %d')}), Decimal('{self.open}'), Decimal('{self.high}'), Decimal('{self.low}'), Decimal('{self.close}'), {self.volume})"

class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def __repr__(self):
        return f'Trade(symbol={self.symbol}, timestamp={self.timestamp}, order={self.order}, price={self.price}, volume={self.volume}, commission={self.commission})'

# Marshmallow schemas
class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(attribute='open') # Use 'attribute' to map to 'open_'
    high = fields.Decimal()
    low = fields.Decimal()
    close = fields.Decimal()
    volume = fields.Int()
    def __repr__(self):
        #formatted_date = self.date.strftime('%Y, %m, %d')
        return f"Stock('{self.symbol}', Date({self.date.strftime('%Y, %m, %d')}), Decimal('{self.open}'), Decimal('{self.high}'), Decimal('{self.low}'), Decimal('{self.close}'), {self.volume})"

   # Add a post_load decorator to create a Stock object after loading data
    @post_load
    def make_stock(self, data, **kwargs):
        # Rename 'open' key back to 'open_' for Stock object creation
        data['open_'] = data.pop('open')
        return Stock(**data)

class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal()
    volume = fields.Int()
    commission = fields.Decimal()
    def __repr__(self):
        return f'Trade(symbol={self.symbol}, timestamp={self.timestamp}, order={self.order}, price={self.price}, volume={self.volume}, commission={self.commission})'
    # Add a post_load decorator to create a Trade object after loading data
    @post_load
    def make_trade(self, data, **kwargs):
        return Trade(**data)
    

class CustomEncoder(json.JSONEncoder):
       #json.dumps is called with the data and the CustomEncoder.
       #CustomEncoder.default is called for each object in the data.
       #If the object is a Stock or Trade, it's handled by the custom logic.
       #If the object is an empty list (or any other type not explicitly handled), the super().default(obj) line
       #Is executed, which calls the parent class's default method.
       #The parent class's default method handles encoding the empty list as [].'''

        def default(self, obj):
            if isinstance(obj, (Stock, Trade)):
            # Create a dictionary with object data and type information
                data = obj.__dict__.copy()

                data['__type__'] = obj.__class__.__name__


            # Handle date, datetime, and Decimal objects
                for key, value in data.items():
                    if isinstance(value, (date, datetime)):
                        data[key] = value.isoformat()
                    elif isinstance(value, Decimal):
                        data[key] = str(value)
                    elif isinstance(value,int):
                        data[key] = f"{value:_}"
                if 'open' in data:
                    data['open_'] = data['open']  # Rename 'open' to 'open_'
                    del data['open'] # Delete 'open' key
                return data

            return super().default(obj)  # Default encoding for other types

def custom_decoder(data):
    if '__type__' in data:
        if data['__type__'] == 'Stock':
            del data['__type__']
            if isinstance(data['open_'], str) | isinstance(data['high'], str) | isinstance(data['low'], str) | isinstance(data['close'], str) | isinstance(data['volume'], str) | isinstance(data['date'], str):# convert open_ to decimal
                  data['open_'] = Decimal(data['open_'])
                  data['high'] = Decimal(data['high'])
                  data['low'] = Decimal(data['low'])
                  data['close'] = Decimal(data['close'])
                  data['volume'] = int(data['volume'])
                  data['volume'] = f"{data['volume']:_}"
                  data['date'] = date.fromisoformat(data['date'])  # Changed line

            return Stock(**data)
        elif data['__type__'] == 'Trade':
            del data['__type__']
            if isinstance(data['timestamp'], str) | isinstance(data['order'], str) | isinstance(data['price'], str) | isinstance(data['commission'], str) | isinstance(data['volume'], str) :
                data['timestamp'] = datetime.fromisoformat(data['timestamp'])
                data['price'] = Decimal(data['price'])
                data['commission'] = Decimal(data['commission'])
                data['volume'] = int(data['volume'])
                data['volume'] = f"{data['volume']:_}"
            return Trade(**data)
    return data  # Return data as is for other types

def serialize_with_marshmallow(obj):
  """Serialize an object using Marshmallow based on its type."""
  if isinstance(obj, Stock):
    schema = StockSchema()
  elif isinstance(obj, Trade):
    schema = TradeSchema()
  else:
    raise ValueError("Unsupported object type for serialization")
  schema_dump = schema.dump(obj)
  # Convert Decimal objects to strings before serializing with json.dumps
  def decimal_to_str(obj):
        if isinstance(obj, Decimal):
            return str(obj)
        raise TypeError

  json_string = json.dumps(schema_dump, default=decimal_to_str)
  return json_string


def deserialize_with_marshmallow(json_string, schema):
  """Deserialize a JSON string using Marshmallow."""
  data = json.loads(json_string)
  return schema.load(data)