#!usr/bin/python
import os
import optparse  

#-----------------------------------------------

# 1) edit script depending if you copy from eos-to-rome or from rome-to-eos (see @--@ below)

# 2) create input list

 # a) example of input list from RomeT2
 # ls /pnfs/roma1.infn.it/data/cms//store/user/gdimperi/Dijet/data/Run2015B_JetHT_12June2015DCSJson_JECV5_4422c9ba9d/JetHT/crab_JetHT__Run2015B-PromptReco-v1__MINIAOD/150712_211959/0000/ | awk '{ print "/pnfs/roma1.infn.it/data/cms//store/user/gdimperi/Dijet/data/Run2015B_JetHT_12June2015DCSJson_JECV5_4422c9ba9d/JetHT/crab_JetHT__Run2015B-PromptReco-v1__MINIAOD/150712_211959/0000/"$0}' > /tmp/list.txt

 # b) example of input list from eos
 # eos ls /eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/santanas/Run2015B_JetHT_12June2015DCSJson_JECV5_4422c9ba9d_150712_211959/ | awk '{print "/eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/santanas/Run2015B_JetHT_12June2015DCSJson_JECV5_4422c9ba9d_150712_211959/"$0}' > /tmp/list.txt

# 3) start the copy
# example:  python romaT2toEOS.py --inputList list.txt --outputDir /pnfs/roma1.infn.it/data/cms/store/user/santanas/rootTrees/Spring15_v1/
#example of eos path: /eos/cms/store/group/phys_exotica/dijet/Dijet13TeV/juska/Spring15_JECV5/RSGravitonToQuarkQuark_kMpl01_M_9000_TuneCUETP8M1_13TeV_pythia8__RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1__MINIAODSIM_9.root

#-----------------------------------------------

usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("--inputList",action="store",type="string",dest="INPUTLIST")
parser.add_option("--outputDir",action="store",type="string",dest="OUTPUTDIR")

(options, args) = parser.parse_args()
INPUTLIST = options.INPUTLIST
OUTPUTDIR = options.OUTPUTDIR

ins = open( INPUTLIST, "r" )
for line in ins:
    line.rstrip('\n')
    #print ("%s" % line)
    #print ("%s" % line)
    head, tail = os.path.split(line)
    head = head.rstrip('\n')
    tail = tail.rstrip('\n')
    #print("%s" % tail)

#####################################################################33
    ##rome to eos @--@
    cmd =  ("lcg-cp -b --vo cms -D srmv2 -U srmv2 -v \"srm://cmsrm-se01.roma1.infn.it:8443/srm/managerv2?SFN=/%s\" \"srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/%s/%s\" " %  (line, OUTPUTDIR, tail)  )
    ##eos to rome @--@
    #cmd =  ("lcg-cp -b --vo cms -D srmv2 -U srmv2 -v \"srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/%s\" \"srm://cmsrm-se01.roma1.infn.it:8443/srm/managerv2?SFN=/%s/%s\" " %  (line, OUTPUTDIR, tail)  )
#####################################################################33

    print cmd    
    
    #check if file already exists
    if (os.path.exists("%s/%s" % (OUTPUTDIR, tail)) == True):
        print("WARNING: File %s already exists in the destination! I'm not overwriting!" % tail)
    else:
        os.system(cmd)

ins.close()
