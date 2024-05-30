# ---------- imports START
import csv
import os
import sys
# ---------- imports END


class GridReference:
    def __init__(self, grid_id, grid_ref):
        self.grid_id = grid_id
        self.grid_ref = grid_ref.replace(" ", "")
        self.ref_length = len(self.grid_ref)
        self.ref_letters = self.grid_ref[:2]
        self.conversion_chart = self.load_conversion_chart()

    def load_conversion_chart(self):
        chart = []
        file_path = os.path.join(os.path.dirname(
            __file__), 'data', 'gr-conversion-chart.csv')
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                chart.append(row)
        return chart

    def is_valid(self):
        if self.grid_ref and self.ref_letters.isalpha():
            if self.ref_length == 2:
                return True
            digits = self.grid_ref[2:]
            if len(digits) % 2 == 0:
                try:
                    int(digits)
                    return True
                except ValueError:
                    pass
        return False

    def convert_xy(self, center_coordinates=False):
        if self.is_valid():

            for grid_square in self.conversion_chart:
                if grid_square['100km_ref'] == self.ref_letters:
                    e_origin = int(grid_square['easting']) * 100000
                    n_origin = int(grid_square['northing']) * 100000

                    if self.ref_length > 2:
                        digits = self.grid_ref[2:]
                        half_digits_length = len(digits)//2
                        scale_factor = 10**(5-half_digits_length)
                        easting = e_origin + \
                            int(digits[:half_digits_length])*scale_factor
                        northing = n_origin + \
                            int(digits[half_digits_length:])*scale_factor

                        if center_coordinates:
                            # plotting in the center of the grid-square (optional)
                            midpoint_offset = 0.5 * scale_factor
                            easting += midpoint_offset
                            northing += midpoint_offset

                    else:
                        if center_coordinates:
                            # plotting in the center of the grid-square (optional)
                            easting = e_origin + 50000
                            northing = n_origin + 50000
                        else:
                            # plotting in the bottom-left corner (conventional)
                            easting = e_origin
                            northing = n_origin

                    # convert coordinates to integers
                    easting = int(easting)
                    northing = int(northing)

                    return {
                        "id": self.grid_id,
                        "gridRef": self.grid_ref,
                        "easting": easting,
                        "northing": northing,
                    }

        # Default return dictionary if not valid or no matching entry found
        return {
            "id": self.grid_id,
            "gridRef": self.grid_ref,
            "easting": "",
            "northing": "",
        }


def main():
    pass


"""
# idiom to set up additional entry point allowing use of class and methods
# from the command line. Not really necessary since this will be a plugin
# if the script is called from command line, the main() function will be called
"""
if __name__ == "__main__":
    main()
