"""
BOOTCAMPERS TO COMPLETE.

Travel to designated waypoint.
"""
# Disable for bootcamp use
# pylint: disable=unused-import


from .. import commands
from .. import drone_report
from .. import drone_status
from .. import location
from ..private.decision import base_decision


# Disable for bootcamp use
# pylint: disable=unused-argument,line-too-long


# All logic around the run() method
# pylint: disable-next=too-few-public-methods
class DecisionSimpleWaypoint(base_decision.BaseDecision):
    """
    Travel to the designed waypoint.
    """
    def __init__(self, waypoint: location.Location, acceptance_radius: float):
        """
        Initialize all persistent variables here with self.
        """
        self.waypoint = waypoint
        print("Waypoint: " + str(waypoint))

        self.acceptance_radius = acceptance_radius

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============
        self.commands =[commands.Command.create_set_relative_destination_command(waypoint.location_x, waypoint.location_y),
                        commands.Command.create_land_command()]
        self.at_destination = False
        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

    def run(self,
            report: drone_report.DroneReport,
            landing_pad_locations: "list[location.Location]") -> commands.Command:
        """
        Make the drone fly to the waypoint.

        You are allowed to create as many helper methods as you want,
        as long as you do not change the __init__() and run() signatures.

        This method will be called in an infinite loop, something like this:

        ```py
        while True:
            report, landing_pad_locations = get_input()
            command = Decision.run(report, landing_pad_locations)
            put_output(command)
        ```
        """
        # Default command
        command = commands.Command.create_null_command()

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============
        def get_position_radius(dron_position: "location.Location") -> float:
            return dron_position.location_x ** 2 + dron_position.location_y ** 2

        # Do something based on the report and the state of this class...
        if report.status == drone_status.DroneStatus.HALTED and not self.at_destination:
            command = self.commands[0]
            self.at_destination = True
        elif report.status == drone_status.DroneStatus.HALTED and self.at_destination:
            command = self.commands[1]
        
        if report.status == drone_status.DroneStatus.HALTED and get_position_radius(report.position) >= self.acceptance_radius:
            command = self.commands[1]
        
    
        
        # Remove this when done
        #raise NotImplementedError

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

        return command
