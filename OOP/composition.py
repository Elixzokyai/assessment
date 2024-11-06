
# composition is a design principle that involves building complex functionality by combining simpler, reusable components or classes, rather than using inheritance alone.

class Engine:
    def __init__(self):
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print("Engine stopped.")
        else:
            print("Engine is already stopped.")


class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def start_engine(self):
        self.engine.start()  # Car uses Engine's start method

    def stop_engine(self):
        self.engine.stop()  # Car uses Engine's stop method

    def is_engine_running(self):
        return self.engine.is_running  # Check if the engine is running


# Example usage:
my_car = Car()
my_car.start_engine()  # Starts the engine
my_car.stop_engine()   # Stops the engine
