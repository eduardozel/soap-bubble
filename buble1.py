import PartDesignGui
import math

docName = "Buble"
extRadius = 7.
clThick = 2
prHeight  = 2.6
prThick = 0.2


def cilinder():

    scClName = 'Sketch'
    App.newDocument( docName )
    App.setActiveDocument( docName )
    App.ActiveDocument=App.getDocument( docName )
    Gui.ActiveDocument=Gui.getDocument( docName )
    App.activeDocument().addObject('PartDesign::Body','Body')
    Gui.activeView().setActiveObject('pdBody', App.activeDocument().Body)
    Gui.Selection.clearSelection()
    Gui.Selection.addSelection(App.ActiveDocument.Body)
    App.ActiveDocument.recompute()
    App.activeDocument().Body.newObject('Sketcher::SketchObject',scClName)
    App.activeDocument().Sketch.Support = (App.activeDocument().XY_Plane, [''])
    App.activeDocument().Sketch.MapMode = 'FlatFace'
    App.ActiveDocument.recompute()
    Gui.activeDocument().setEdit( scClName )
    intRadius = extRadius - clThick
    ActiveSketch = App.ActiveDocument.getObject('Sketch')
    clCenter = App.Vector( 0., 0., 0 )
    App.ActiveDocument.Sketch.addGeometry( Part.Circle( clCenter, App.Vector( 0, 0, 1 ), extRadius), False )
    App.ActiveDocument.Sketch.addConstraint( Sketcher.Constraint('Coincident', 0,  3, -1, 1)) 
    App.ActiveDocument.recompute()
    App.ActiveDocument.Sketch.addGeometry( Part.Circle( clCenter, App.Vector(0,0,1), intRadius),False)
    App.ActiveDocument.Sketch.addConstraint( Sketcher.Constraint('Coincident', 1,  3, -1, 1) ) 
    App.ActiveDocument.recompute()
    Gui.getDocument( docName ).resetEdit()
    App.activeDocument().Body.newObject("PartDesign::Pad","Pad")
    App.activeDocument().Pad.Profile = App.activeDocument().Sketch
    App.activeDocument().Pad.Length = 1.0
    App.ActiveDocument.recompute()
    Gui.activeDocument().hide( scClName )
    App.ActiveDocument.recompute()
    Gui.activeDocument().setEdit('Pad', 0)
    Gui.Selection.clearSelection()
    Gui.ActiveDocument.Pad.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
    Gui.ActiveDocument.Pad.LineColor=Gui.ActiveDocument.Body.LineColor
    Gui.ActiveDocument.Pad.PointColor=Gui.ActiveDocument.Body.PointColor
    Gui.ActiveDocument.Pad.Transparency=Gui.ActiveDocument.Body.Transparency
    Gui.ActiveDocument.Pad.DisplayMode=Gui.ActiveDocument.Body.DisplayMode
    Gui.activeDocument().hide( scClName )
    App.ActiveDocument.Pad.Length = 1.
    App.ActiveDocument.Pad.Length2 = 100.
    App.ActiveDocument.Pad.Type = 0
    App.ActiveDocument.Pad.UpToFace = None
    App.ActiveDocument.Pad.Reversed = 0
    App.ActiveDocument.Pad.Midplane = 0
    App.ActiveDocument.Pad.Offset = 0.
    App.ActiveDocument.recompute()
    Gui.activeDocument().resetEdit()
    Gui.SendMsgToActiveView("ViewFit")

def paral():
    def multiply():
        App.activeDocument().Body.newObject("PartDesign::Pad","Pad001")
        App.activeDocument().Pad001.Profile = App.activeDocument().Sketch001
        App.activeDocument().Pad001.Length = 10.0
        App.ActiveDocument.recompute()
        Gui.activeDocument().hide("Sketch001")
        App.ActiveDocument.recompute()
        Gui.activeDocument().setEdit('Pad001', 0)
        Gui.Selection.clearSelection()
        Gui.ActiveDocument.Pad001.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
        Gui.ActiveDocument.Pad001.LineColor=Gui.ActiveDocument.Body.LineColor
        Gui.ActiveDocument.Pad001.PointColor=Gui.ActiveDocument.Body.PointColor
        Gui.ActiveDocument.Pad001.Transparency=Gui.ActiveDocument.Body.Transparency
        Gui.ActiveDocument.Pad001.DisplayMode=Gui.ActiveDocument.Body.DisplayMode
        Gui.activeDocument().hide("Sketch001")
        App.ActiveDocument.Pad001.Length = 2.
        App.ActiveDocument.Pad001.Length2 = 100.
        App.ActiveDocument.Pad001.Type = 0
        App.ActiveDocument.Pad001.UpToFace = None
        App.ActiveDocument.Pad001.Reversed = 0
        App.ActiveDocument.Pad001.Midplane = 0
        App.ActiveDocument.Pad001.Offset = 0.
        Gui.activeDocument().hide("Pad")
        App.ActiveDocument.recompute()
        Gui.activeDocument().resetEdit()
        App.activeDocument().Body.newObject("PartDesign::PolarPattern","PolarPattern")
        App.ActiveDocument.recompute()
        App.activeDocument().PolarPattern.Originals = [App.activeDocument().Pad001,]
        App.activeDocument().PolarPattern.Axis = (App.activeDocument().Sketch001, ["N_Axis"])
        App.activeDocument().PolarPattern.Angle = 360
        App.activeDocument().PolarPattern.Occurrences = 27
        App.ActiveDocument.recompute()
        Gui.activeDocument().setEdit('PolarPattern', 0)
        Gui.Selection.clearSelection()
        Gui.ActiveDocument.PolarPattern.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
        Gui.ActiveDocument.PolarPattern.LineColor=Gui.ActiveDocument.Body.LineColor
        Gui.ActiveDocument.PolarPattern.PointColor=Gui.ActiveDocument.Body.PointColor
        Gui.ActiveDocument.PolarPattern.Transparency=Gui.ActiveDocument.Body.Transparency
        Gui.ActiveDocument.PolarPattern.DisplayMode=Gui.ActiveDocument.Body.DisplayMode
        App.activeDocument().Body.Tip = App.activeDocument().PolarPattern
        Gui.activeDocument().show("PolarPattern")
        App.ActiveDocument.recompute()
        App.ActiveDocument.PolarPattern.Originals = [App.ActiveDocument.Pad001,]
        Gui.activeDocument().hide("Pad001")
        App.ActiveDocument.recompute()
        Gui.activeDocument().resetEdit()
	
    Gui.activeDocument().activeView().viewTop()
    App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch001')
    App.activeDocument().Sketch001.Support = (App.activeDocument().XY_Plane, [''])
    App.activeDocument().Sketch001.MapMode = 'FlatFace'
    App.ActiveDocument.recompute()
    Gui.activeDocument().setEdit('Sketch001')
    extPoint = extRadius + 0.3
    intPoint = extPoint  - prHeight
    geoList = []
    v1pLine1 = App.Vector( -prThick, extPoint, 0)
    v1pLine2 = App.Vector(  prThick, extPoint, 0)
    geoList.append(Part.LineSegment( v1pLine1, v1pLine2))
    v2pLine1 = App.Vector( prThick, extPoint, 0)
    v2pLine2 = App.Vector( prThick, intPoint, 0)
    geoList.append(Part.LineSegment( v2pLine1, v2pLine2))
    v3pLine1 = App.Vector(  prThick, intPoint, 0)
    v3pLine2 = App.Vector( -prThick, intPoint, 0)
    geoList.append(Part.LineSegment( v3pLine1, v3pLine2))
    v4pLine1 = App.Vector( -prThick, intPoint, 0)
    v4pLine2 = App.Vector( -prThick, extPoint, 0)
    geoList.append(Part.LineSegment( v4pLine1, v4pLine2))
    App.ActiveDocument.Sketch001.addGeometry(geoList,False)
    conList = []
    conList.append(Sketcher.Constraint('Coincident', 0, 2,1,1))
    conList.append(Sketcher.Constraint('Coincident', 1 ,2,2,1))
    conList.append(Sketcher.Constraint('Coincident', 2 ,2,3,1))
    conList.append(Sketcher.Constraint('Coincident', 3 ,2,0,1))
    conList.append(Sketcher.Constraint('Horizontal', 0))
    conList.append(Sketcher.Constraint('Horizontal', 2))
    conList.append(Sketcher.Constraint('Vertical',1))
    conList.append(Sketcher.Constraint('Vertical',3))
    App.ActiveDocument.Sketch001.addConstraint(conList)
    App.ActiveDocument.recompute()
    App.getDocument(docName).recompute()
    multiply()
    Gui.SendMsgToActiveView("ViewFit")

def multCirc():

    def clPlace( n ):
        nmBody = '{}{}'.format( 'Body00', n )
        if n==0:
            nmBody = 'Body'

        print ( nmBody )

        u = n * 360. / 7
        ur = math.radians( u )
        radius = 19.
        x = math.cos( ur ) * radius
        y = math.sin( ur ) * radius
        crVec = App.Vector(  x, y, 0 )
        FreeCAD.getDocument( docName ).getObject(nmBody).Placement = App.Placement(  crVec, App.Rotation( App.Vector( 0, 0, 0 ), 0 ) )
        bx = App.ActiveDocument.addObject("Part::Box","Box")
        bx.Height = '2 mm'
        bx.Width  = '2 mm'
        bx.Length = '14. mm'
        vb = App.Vector( 0, 0, 0 )
        vr = App.Vector( 0, 0, 1 )
        bx.Placement = App.Placement( vb, App.Rotation( vr , u ) )

    def simpCopy( n ):
        App.ActiveDocument.addObject('Part::Feature','Body').Shape=App.ActiveDocument.Body.Shape
        App.ActiveDocument.ActiveObject.Label=App.ActiveDocument.Body.Label
        Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
        Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Body.LineColor
        Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Body.PointColor
        Gui.ActiveDocument.ActiveObject.DiffuseColor=Gui.ActiveDocument.Body.DiffuseColor
        App.ActiveDocument.recompute()

    simpCopy(1)
    simpCopy(2)
    simpCopy(3)
    simpCopy(4)
    simpCopy(5)
    simpCopy(6)

    clPlace( 0 )
    clPlace( 1 )
    clPlace( 2 )
    clPlace( 3 )
    clPlace( 4 )
    clPlace( 5 )
    clPlace( 6 )

    App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
    App.ActiveDocument.ActiveObject.Label = "center"
    FreeCAD.getDocument("Buble").getObject("Cylinder").Radius = '4 mm'
    FreeCAD.getDocument("Buble").getObject("Cylinder").Height = '2 mm'
    App.ActiveDocument.recompute()
    App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
    App.ActiveDocument.ActiveObject.Label = "hole"
    FreeCAD.getDocument("Buble").getObject("Cylinder001").Radius = '1 mm'
    FreeCAD.getDocument("Buble").getObject("Cylinder001").Height = '3 mm'

    App.activeDocument().addObject("Part::Cut","Cut")
    App.activeDocument().Cut.Base = App.activeDocument().Cylinder
    App.activeDocument().Cut.Tool = App.activeDocument().Cylinder001
    Gui.activeDocument().Cylinder.Visibility=False
    Gui.activeDocument().Cylinder001.Visibility=False
    Gui.ActiveDocument.Cut.ShapeColor=Gui.ActiveDocument.Cylinder.ShapeColor
    Gui.ActiveDocument.Cut.DisplayMode=Gui.ActiveDocument.Cylinder.DisplayMode
    App.ActiveDocument.recompute()

#    App.ActiveDocument.addObject("Part::Box","Box")
#    FreeCAD.getDocument("Buble").getObject("Box").Height = '1 mm'
#    FreeCAD.getDocument("Buble").getObject("Box").Width  = '1 mm'
#    FreeCAD.getDocument("Buble").getObject("Box").Length = '6 mm'
#    vb = App.Vector( 3.5, -0.5, 0 )
#    FreeCAD.getDocument("Buble").getObject("Box").Placement = App.Placement( vb, App.Rotation(App.Vector(0,0,1),0 ) )
#    App.ActiveDocument.recompute()

# ================= MAIN =================

cilinder()
paral()
multCirc()
Gui.SendMsgToActiveView("ViewFit")
