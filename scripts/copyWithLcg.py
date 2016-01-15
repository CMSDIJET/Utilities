#!usr/bin/python
import os
import optparse 
import sys 
import subprocess
import re


usage = "run it from the site that contains the input directory: python copyWithLcg.py  --inputStorage ROME --inputDir /pnfs/roma1.infn.it/data/cms/store/user/santanas/Dijet13TeVScouting/rootTrees_big/TEST/ --outputStorage CERN --outputDir /eos/cms/store/group/phys_exotica/dijet/Dijet13TeVScouting/rootTrees_big/TEST/"
parser = optparse.OptionParser(usage)
parser.add_option("--inputStorage",action="store",type="string",dest="INPUTSTORAGE")
parser.add_option("--outputStorage",action="store",type="string",dest="OUTPUTSTORAGE")
parser.add_option("--inputDir",action="store",type="string",dest="INPUTDIR")
parser.add_option("--outputDir",action="store",type="string",dest="OUTPUTDIR")

(options, args) = parser.parse_args()
INPUTSTORAGE = options.INPUTSTORAGE
INPUTDIR = options.INPUTDIR
OUTPUTSTORAGE = options.OUTPUTSTORAGE
OUTPUTDIR = options.OUTPUTDIR

storagePath = {'ROME': "srm://cmsrm-se01.roma1.infn.it:8443/srm/managerv2?SFN=/", 
               'CERN': "srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/"}

out = ""
if INPUTSTORAGE == 'CERN':
    print INPUTSTORAGE
    proc = subprocess.Popen(["/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls %s | grep root" % INPUTDIR], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
if INPUTSTORAGE == 'ROME':
    print INPUTSTORAGE
    proc = subprocess.Popen(["ls %s | grep root" % INPUTDIR], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

out = out.splitlines()

for infile in out:
    infile.rstrip('\n')
    inpath = INPUTDIR+infile
    inpath.rstrip('\n')
    #print inpath

    ##rome to eos @--@
    cmd =  ("lcg-cp -b --vo cms -D srmv2 -U srmv2 -v \"%s%s\" \"%s%s/%s\" " %  (storagePath[INPUTSTORAGE],inpath,storagePath[OUTPUTSTORAGE],OUTPUTDIR,infile)  )
    #print cmd    

    #check if file already exists
    checkfilecommand = "lcg-ls -b --vo cms -D srmv2 -v \"%s%s/%s\" " %  (storagePath[OUTPUTSTORAGE],OUTPUTDIR,infile)
    proc = subprocess.Popen(["lcg-ls -b --vo cms -D srmv2 -v \"%s%s/%s\" " %  (storagePath[OUTPUTSTORAGE],OUTPUTDIR,infile)], stdout=subprocess.PIPE, shell=True)
    (checkfile, err) = proc.communicate()
    checkfile = checkfile.splitlines()
    print checkfile

    if len(checkfile)==2:
        print("WARNING: File \"%s%s/%s\" already exists in the destination! I'm not overwriting!" %  (storagePath[OUTPUTSTORAGE],OUTPUTDIR,infile))
    if len(checkfile)==1:
        print "I'll start the copy"
        print cmd
        os.system(cmd)

