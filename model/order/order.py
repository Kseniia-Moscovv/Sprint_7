class Order:
    def __init__(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.metro_station = metro_station
        self.phone = phone
        self.rent_time = rent_time
        self.delivery_date = delivery_date
        self.comment = comment
        self.color = color

    def to_dict(self):
        return {
            'firstName': self.first_name,
            'lastName': self.last_name,
            'address': self.address,
            'metroStation': self.metro_station,
            'phone': self.phone,
            'rentTime': self.rent_time,
            'deliveryDate': self.delivery_date,
            'comment': self.comment,
            'color': self.color
        }
