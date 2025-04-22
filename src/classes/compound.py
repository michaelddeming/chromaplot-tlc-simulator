from typing import Optional

"""Class for Compounds, consiting of an name, x-coordinate, y-coordinate, and retention-factor. 
    - Methods to alter those attributes."""

class Compound:

    def __init__(self, name: str, x_cord: int, y_cord: int, ret_fact: float):

        self.name = name    
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.ret_fact = ret_fact


    # UPDATE FUNCTIONS
    def update_data(self, new_x_cord: int, new_y_cord: int, new_ret_fact: Optional[int]) -> None:
        """Update the x and y coordinates of the Compound. Returns None. Compound.new_ret_fact=Optional update parameter."""

        # required params
        if not (isinstance(new_x_cord, int) and isinstance(new_y_cord, int)):
            raise ValueError(f"Error: Attr -> {new_x_cord} or {new_y_cord} not Integer!")
        self.x_cord, self.y_cord = new_x_cord, new_y_cord

        # optional params
        if new_ret_fact:
            if not isinstance(new_ret_fact, int):
                raise ValueError(f"Error: Attr -> {new_ret_fact} not Integer!")
            self.ret_fact = new_ret_fact
    
    # GET_FUNCTIONS
    def get_all(self) -> list:
        """Get all information related to a Compound, returned in a list."""
        return [value for value in self.__dict__.values()]
    
    def get_data(self) -> list:
        """Get all integer/float data related to a Compound, returned in a list."""
        return [value for key, value in self.__dict__.items() if key != "name"]
    
    def get_coords(self) -> list:
        """Get x_cord and y_cord, each within its own list, remains compatible with matplotlib."""
        return [self.x_cord], [self.y_cord]
