#!usr/bin/python
import os
import optparse 
import sys 
import subprocess

usage = "usage: %prog [options]"
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

out = ()

if INPUTSTORAGE == 'CERN':
    print INPUTSTORAGE
    proc = subprocess.Popen(["eos ls %s | grep root" % INPUTDIR], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
if INPUTSTORAGE == 'ROME':
    print INPUTSTORAGE
    proc = subprocess.Popen(["ls %s | grep root" % INPUTDIR], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

print "program output:", out
out = out.splitlines()

for infile in out:
    infile.rstrip('\n')
    inpath = INPUTDIR+infile
    inpath.rstrip('\n')
    #print inpath

    ##rome to eos @--@
    cmd =  ("lcg-cp -b --vo cms -D srmv2 -U srmv2 -v \"%s%s\" \"%s%s/%s\" " %  (storagePath[INPUTSTORAGE],inpath,storagePath[OUTPUTSTORAGE],OUTPUTDIR,infile)  )

    print cmd    
