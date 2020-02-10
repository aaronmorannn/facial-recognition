 function goPython(){
       $.ajax({
  		     url: "../../python_files/camera.py",
             context: document.body
             }).done(function() {
             alert('finished python script');;
            });
  }
