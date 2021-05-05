# Collect stats for COSMIC

import logging
import evla_mcast

# Set log format, level
logging.basicConfig(format="%(asctime)-15s %(levelname)8s %(message)s",
        level=logging.INFO)

class SimpleController(evla_mcast.Controller):

    def __init__(self):

        # Call base class init
        super(SimpleController, self).__init__()

        # Require two Observation XML documents in order to get
        # the scan stop time as well as basic scan metadata:
        self.scans_require = ['obs', 'stop']

    def handle_config(self, scan):

        NANT = scan.numAntenna
        BW = scan.get_receiver('BD')
        SRC = scan.source
        IFids = scan.IFids
        FCENTs=[]
        for i in IFids:
            FCENTs.append(scan.get_sslo(i))
        RA  = scan.ra_deg
        DEC = scan.dec_deg
        TSTART = scan.startTime
        TEND = scan.stopTime
        PROJID = scan.projid
        #STATION = scan.listOfStations
        MJD = str(TSTART).split('.')[0]
        with open("vla_output_MJD"+MJD+".dat", 'a') as f:
            print("PROJID= %s SRC= %s (ra,dec)=( %.3f , %.3f ) deg | MJD= %.6f - %.6f | NANT= %d "
                  % (PROJID, SRC, RA, DEC, TSTART, TEND, NANT), BW, len(FCENTs), FCENTs, file=f)
        f.close()

c = SimpleController()
c.run()
