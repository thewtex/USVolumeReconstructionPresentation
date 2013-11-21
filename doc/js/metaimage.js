window.onload = function() {

  // create and initialize a 3D renderer
  var r = new X.renderer2D();
  //r.container = 'sliceZ';
  r.orientation = 'Z';
  r.bgColor = [.2, .2, 0.2];
  r.init();

  // create a X.volume
  var volume = new X.volume();
  // .. and attach the single-file dicom in .NRRD format
  // this works with gzip/gz/raw encoded NRRD files but XTK also supports other
  // formats like MGH/MGZ
  volume.file = 'data/SubSequence.nii';

  // only add the volume for now, the mesh gets loaded on request
  r.add(volume);

  r.render();

  // the onShowtime method gets executed after all files were fully loaded and
  // just before the first rendering attempt
  r.onShowtime = function() {

    //
    // The GUI panel
    //
    // (we need to create this during onShowtime(..) since we do not know the
    // volume dimensions before the loading was completed)

    var gui = new dat.GUI();

    // the following configures the gui for interacting with the X.volume
    var volumegui = gui.addFolder('Volume');
    // now we can configure controllers which..
    // .. switch between slicing and volume rendering
    //var vrController = volumegui.add(volume, 'volumeRendering');
    // the min and max color which define the linear gradient mapping
    var minColorController = volumegui.addColor(volume, 'minColor');
    var maxColorController = volumegui.addColor(volume, 'maxColor');
    var lowerWindowController = volumegui.add(volume, 'windowLow', volume.min,
        volume.max);
    var upperWindowController = volumegui.add(volume, 'windowHigh', volume.min,
        volume.max);
    // the indexX,Y,Z are the currently displayed slice indices in the range
    // 0..dimensions-1
    var sliceZController = volumegui.add(volume, 'indexZ', 0,
        volume.range[2] - 1);
    volumegui.open();
  };

  // adjust the camera position a little bit, just for visualization purposes
  //r.camera.position = [120, 80, 160];

  // showtime! this triggers the loading of the volume and executes
  // r.onShowtime() once done
  r.render();

};
