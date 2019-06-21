# URScript Move
There are several ways to move the [TCP](TCP.md) to a desired position, called a [waypoint](Waypoint.md). You will have to choose the correct command depending on the action you want to perform otherwise you could axidentl into objects or trigger the safty mechanisms.

## Move L - Linear Move
This command is used to move the TCP  over a linear path to a specific waypoint. This means that it will move the TCP from a waypoint (or its current location) to an other waypoint in a strait path. This command is commonly used when placing or lifting up a object, you want to move the TCP in a straight line without scraping the object over the surface its placed on.

## MoveJ - Joint Move
This command is used to move the TXP over a non liniar path to a specific waypoint.