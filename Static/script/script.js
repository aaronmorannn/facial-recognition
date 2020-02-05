function goPython(){
            $.ajax({
              url: "Code-Snippets/camera.py",
             context: document.body
            }).done(function() {
             alert('Opened python script');;
            });
 }