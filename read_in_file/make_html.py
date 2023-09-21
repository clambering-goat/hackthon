from jinja2 import Template

import read_in
tm = Template(""" 
<!DOCTYPE html>
<html>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<body onload="toggleTable('db_list')">




<h2>A basic HTML table</h2>
<button onclick="toggleTable('full_table')">full_table</button>
<button onclick="toggleTable('db_list')">db_list</button>
<button onclick="toggleTable('has_data')">has_data</button>
<button onclick="toggleTable('missing_data')">missing_data</button>


  <div class="autocomplete" style="width:300px;">
    <input id="myInput" type="text" name="myCountry" placeholder="Country">
  </div>
  
  

<script>

function toggleTable(one_to_keep) {
let xy =document.querySelectorAll('*[id]');
for (let i = 0; i < xy.length; i++) { 
  var x = document.getElementById(xy[i].id);
  x.style.display = "none"; 
}
  var x = document.getElementById(one_to_keep);
  x.style.display = "block";
  var x = document.getElementById('myInput');
  x.style.display = "block";
  
  
}



function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
}

/*An array containing all the country names in the world:*/
var countries ={{list_evey_thing}}
/*initiate the autocomplete function on the "myInput" element, and pass along the countries array as possible autocomplete values:*/
autocomplete(document.getElementById("myInput"), countries);




</script>






<table id="full_table">
{% for item in items %}
<TR>
    {% for item2 in items[item] %}
    <TD ><SPAN>{{item2}}</SPAN></TD>
    {% endfor %}
</TR>
{% endfor %}
</table>


<table id="db_list">
{% for item in list_db %}
<TR>
    <TD ><SPAN>{{item}}</SPAN></TD>
        <TD ><SPAN>{{db_data[item]}}</SPAN></TD>
</TR>
{% endfor %}
</table>




<table id="missing_data">
{% for item in has_data %}
<TR>
    {% for item2 in item %}
    <TD ><SPAN>{{item2}}</SPAN></TD>
    {% endfor %}
</TR>
{% endfor %}
</table>

<table id="has_data">
{% for item in missing_data %}
<TR>
    {% for item2 in item %}
    <TD ><SPAN>{{item2}}</SPAN></TD>
    {% endfor %}
</TR>
{% endfor %}
</table>





<p>To understand the example better, we have added borders to the table.</p>





</body>
</html>
""")
full_data,has_data,list_db,db_data,list_evey_thing,missing_data=read_in.run_get_array_data()

msg = tm.render(items=full_data,has_data=has_data,list_db=list_db,db_data=db_data,list_evey_thing=list_evey_thing,missing_data=missing_data)
file=open("./html_demo.html","w")
file.write(msg)
