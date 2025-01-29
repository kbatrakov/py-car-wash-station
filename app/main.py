class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_collection: list) -> float:
        filtered_cars = [car for car in car_collection if car.clean_mark < self.clean_power]
        benefit = round(sum([car.comfort_class * ((self.clean_power - car.clean_mark) * self.average_rating) /
                             self.distance_from_city_center for car in filtered_cars]), 1)

        [self.wash_single_car(car) for car in filtered_cars]
        return benefit

    def calculate_washing_price(self, car):
        return round((car.comfort_class * ((self.clean_power - car.clean_mark)
                                           * self.average_rating)
                      / self.distance_from_city_center), 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        self.count_of_ratings += 1
        self.average_rating = (self.average_rating + rate) // 2
