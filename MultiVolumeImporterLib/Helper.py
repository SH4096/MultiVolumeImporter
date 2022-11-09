from __main__ import vtk, cjyx

class Helper:

  @staticmethod
  def SetBgFgVolumes(bgID, fgID):
    appLogic = cjyx.app.applicationLogic()
    selectionNode = appLogic.GetSelectionNode()
    if bgID is not None:
      selectionNode.SetReferenceActiveVolumeID(bgID)
    if fgID is not None:
      selectionNode.SetReferenceSecondaryVolumeID(fgID)
    appLogic.PropagateVolumeSelection()

