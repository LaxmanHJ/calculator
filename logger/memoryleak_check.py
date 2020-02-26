from pympler.classtracker import ClassTracker

import Factory

tracker=ClassTracker()
tracker=track_class(Factory.main1)
print ("Create data")
tracker.create_snapshot()
data = create_data(tracker)
tracker.create_snapshot()

