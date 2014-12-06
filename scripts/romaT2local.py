#!usr/bin/python
import os
import optparse  

usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("--inputList",action="store",type="string",dest="INPUTLIST")
parser.add_option("--outputDir",action="store",type="string",dest="OUTPUTDIR")

(options, args) = parser.parse_args()
INPUTLIST = options.INPUTLIST
OUTPUTDIR = options.OUTPUTDIR

ins = open( INPUTLIST, "r" )
for line in ins:
    #print ("%s" % line)
    head, tail = os.path.split(line)
    head = head.rstrip('\n')
    tail = tail.rstrip('\n')
    #print("%s" % tail)
    cmd =  ("lcg-cp -b --vo cms -D srmv2 -U srmv2 -v \"srm://cmsrm-se01.roma1.infn.it:8443/srm/managerv2?SFN=%s\" \"file:%s/%s\" " %  (line, OUTPUTDIR, tail)  )
    #print cmd
    
    #check if file already exists
    if (os.path.exists("%s/%s" % (OUTPUTDIR, tail)) == True):
        print("WARNING: File %s already exists in the destination! I'm not overwriting!" % tail)
    else:
        os.system(cmd)

ins.close()
