import ROOT,os,sys,resource,psutil,argparse
from Style import *

DataPeriods = ['Data1516']#, 'Data15', 'Data16']

compareSelections = [
  'nobjetVeto',
  'bjetVeto',
  'allbjetVeto'
]

Observables = [
  'njet',
  'ht', 
  'mT',
  'met',
]

Channel = 'EL'
Selection = 'SR'
Tagger = 'MV2c10'

Debug = False

# Style setups
Colors = {
  'nobjetVeto'  : ROOT.kBlue,
  'bjetVeto'    : ROOT.kRed,
  'allbjetVeto' : ROOT.kOrange-5,
}
LineWidths = {
  'nobjetVeto'  : 3,
  'bjetVeto'    : 2,
  'allbjetVeto' : 2,
}
Labels = {
  'nobjetVeto'  : 'no b-jet Veto',
  'bjetVeto'    : 'nominal',
  'allbjetVeto' : 'b-jet Veto: njet #geq 0',
}

#######################################################################################################
# DO NOT MODIFY (below this line)
#######################################################################################################

os.system('mkdir -p Plots/Significance')

# AtlasStyle
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/j/jbossios/work/public/xAOD/Results/AtlasStyle/AtlasStyle.C")
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(True) # so it doesn't pop up a window

# Loop over data periods
for dataperiod in DataPeriods:
  # Loop over observables
  for histname in Observables:

    # TCanvas
    if Debug: print "DEBUG: Create TCanvas"
    Canvas  = ROOT.TCanvas()
    outName = "Plots/Significance/{0}_{1}_{2}_{3}_{4}.pdf".format(dataperiod,Channel,Selection,Tagger,histname)
    Canvas.Print(outName+"[")

    # TPad for upper panel
    if Debug: print "DEBUG: Create TPad for upper panel"
    pad1 = ROOT.TPad('pad1','pad1',0,0.4,1,1.0)
    pad1.SetTopMargin(0.12)
    pad1.SetBottomMargin(0.03)
    pad1.Draw()
    pad1.cd()

    # TLegend
    if Debug: print "DEBUG: Create TLegend"
    Legends = ROOT.TLegend(0.7,0.6,0.9,0.88)
    Legends.SetTextFont(42)

    # Add histogram (one for each selection) to THStack and draw legends
    for study in compareSelections:

      # Open input file
      FileName = 'OutputROOTFiles/Significance/'+dataperiod+'_'+Channel+'_'+Selection+'_'+Tagger+'_'+histname+'_'+study+'.root'
      File     = ROOT.TFile.Open(FileName,"READ")
      if not File:
        print "ERROR: {} not found, exiting".format(FileName)
	sys.exit(0)

      # Get significance histogram
      hist = File.Get('Significance')
      if not hist:
        print "ERROR: Significance histogram not found, exiting"
	sys.exit(0)
      hist.SetDirectory(0)

      # Print helpful information for njet case when debugging
      if Debug and histname is 'njet':
        # Read significance values for njet
        nbins  = hist.GetNbinsX()
        Svalue = 0 #significance value printed to put in a table
        gtOnejets = 0
        gtTwojets = 0
        for ibin in range(1,nbins+1):
          Svalue = hist.GetBinContent(ibin)
	  print 'DEBUG: ibin = ',ibin-1,'        , Significance Value = ',Svalue 
          if ibin > 0 and ibin < 9: gtOnejets += Svalue 
          if ibin > 1 and ibin < 9: gtTwojets += Svalue 
	print "DEBUG: For "+study+": Significance Value when njet >= 1 is ",gtOnejets
	print "DEBUG: For "+study+": Significance Value when njet >= 2 is ",gtTwojets

      # Set style for each selection
      hist.SetMarkerColor(Colors[study])
      hist.SetLineColorAlpha(Colors[study],0.5)
      hist.SetLineWidth(LineWidths[study])
      hist.Draw("same")
      Legends.AddEntry(hist,Labels[study],"l")
      if XaxisRange.has_key(histname):
        hist.GetXaxis().SetRangeUser(XaxisRange[histname][0],XaxisRange[histname][1])
      pad1.SetLogy()

      # Identify histograms
      if study is 'nobjetVeto':    hist_nobjet  = hist
      elif study is 'bjetVeto':    hist_nom     = hist
      elif study is 'allbjetVeto': hist_allveto = hist

    # Set style
    hist_nobjet.GetXaxis().SetLabelSize(0.)
    hist_nobjet.GetXaxis().SetTitleSize(0.)
    hist_nobjet.GetXaxis().SetLabelSize(0.)
    hist_nobjet.GetXaxis().SetTitleSize(0.)
    hist_nobjet.GetYaxis().SetTitleSize(20)
    hist_nobjet.GetYaxis().SetTitleFont(43)
    hist_nobjet.GetYaxis().SetLabelFont(43)
    hist_nobjet.GetYaxis().SetLabelSize(19)
    hist_nobjet.GetYaxis().SetTitleOffset(1.3)
    hist_nobjet.GetYaxis().SetLabelSize(18)
    hist_nobjet.GetYaxis().SetTitle("S/#sqrt{S+B}")

    # Draw legends
    Legends.Draw("same")
    ROOT.gPad.RedrawAxis()

    # Show ATLAS legend
    atlas = "#scale[1.3]{#scale[1.4]{#font[72]{ATLAS} #font[42]{Internal}}}"
    ATLASBlock = ROOT.TLatex(0.2,0.8,atlas)
    ATLASBlock.SetNDC()
    ATLASBlock.Draw("same")

    # Create TPad for ratio panel
    if Debug: print "DEBUG: Create TPad for bottom panel"
    Canvas.cd()
    pad2 = ROOT.TPad("pad2","pad2",0,0.05,1,0.4)
    pad2.SetTopMargin(0.03)
    pad2.SetBottomMargin(0.42)
    pad2.Draw()
    pad2.cd()
    #if hist in Logx: pad2.SetLogx()

    # Create ratio histograms
    if Debug: print "DEBUG: Create ratio histograms"

    # First draw nom/nobjet histogram
    ratio = hist_nom.Clone('ratio')
    ratio.Divide(hist_nobjet)
    ratio.SetLineColorAlpha(ROOT.kRed,0.5)
    if histname is 'njet': 
      ratio.SetMaximum(3.)
      ratio.SetMinimum(.5)        
    else: 
      ratio.SetMaximum(1.10)
      ratio.SetMinimum(0.80)
      #ratio.GetYaxis().SetNdivisions(5)
    ratio.Draw()

    # Now draw allveto/nobjet histogram
    ratio_allveto = hist_allveto.Clone('ratio')
    ratio_allveto.Divide(hist_nobjet)
    ratio_allveto.SetLineColorAlpha(ROOT.kOrange-5,0.5)
    ratio_allveto.Draw("same")

    # Set style
    ratio.GetXaxis().SetTitleSize(20)
    ratio.GetXaxis().SetTitleFont(43)
    ratio.GetXaxis().SetLabelFont(43)
    ratio.GetXaxis().SetLabelSize(19)
    ratio.GetXaxis().SetTitleOffset(3)
    if histname is 'njet':
      ratio.GetXaxis().SetTitle(histname)
    else:
      ratio.GetXaxis().SetTitle(histname+' [GeV]')
    ratio.GetXaxis().SetNdivisions(510)
    ratio.GetYaxis().SetTitleSize(17)
    ratio.GetYaxis().SetTitleFont(43)
    ratio.GetYaxis().SetLabelFont(43)
    ratio.GetYaxis().SetLabelSize(18)
    ratio.GetYaxis().SetTitleOffset(1.3)
    ratio.GetYaxis().SetTitle("veto / no-veto")

    # Draw line at ratio = 1 in MET vs MTW plot
    if "met_mtw" not in histname and histname in XaxisRange:
      nbins = ratio.GetNbinsX()
      minX = XaxisRange[histname][0]
      maxX = XaxisRange[histname][1]
      if histname is 'njet': maxX += 0.5
      Line = ROOT.TLine(minX,1,maxX,1)
      Line.SetLineStyle(7)
      Line.SetLineColor(16)
      Line.Draw("same")    

    # Save plot
    #Canvas.SetLogx()
    Canvas.cd()
    Canvas.Print(outName)
    Canvas.Print(outName+"]")

# Make MET vs MTW 2D plots for each selection
for study in compareSelections:
  Canvas  = ROOT.TCanvas()
  histname = "met_mtw"
  outName = "Plots/Significance/{0}_{1}_{2}_{3}_{4}_{5}.pdf".format(dataperiod,Channel,Selection,Tagger,histname,study)
  Canvas.Print(outName+"[")
  File = ROOT.TFile.Open('OutputROOTFiles/Significance/'+dataperiod+'_'+Channel+'_'+Selection+'_'+Tagger+'_'+histname+'_'+study+'.root',"READ")
  hist = File.Get('Significance')
  hist.Draw("colz")
  hist.GetXaxis().SetTitle("MET")
  hist.GetYaxis().SetTitle("MTW")
  Canvas.SetLogx()
  Canvas.SetLogy()
  Canvas.Print(outName)
  Canvas.Print(outName+"]")

print ">>> ALL DONE <<<"
