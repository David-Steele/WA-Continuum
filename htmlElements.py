# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 19:59:07 2014
@author: David
"""
header = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" content="HTML, CSS">
<title>Your Alignment Grid(s) :-)</title>
<style>
.table tr:hover td {background-color:#ffff99;background:rgba(0,80,0,0.5);}
/*.table tr:hover th {background-color:#ffff99;background:rgba(0,80,0,0.5);}*/
th.rotate {height: 140px;white-space: nowrap}
th.rotate > div {transform: translate(0px, 68px)rotate(310deg);width: 16px;}
th.rotate > div > span {border-bottom: 0px solid #ccc; padding: 2px 10px;}

.table-header-rotated {/*border-collapse: collapse;*/ 
	.csstransforms & td {width: 20px;}
	.no-csstransforms & th { padding: 5px 10px;}
  td {text-align: center;padding: 2px 2px;border: 0px solid #ccc;}
  
  /* .csstransforms & th.rotate {height: 140px;white-space: nowrap;
   /* // Firefox needs the extra DIV, otherwise the text disappears if you rotate 
    > div {
      transform: translate(18px, 51px)rotate(310deg);width: 30px;}
    > div > span {border-bottom: 1px solid #ccc;padding: 5px 10px;}}
  th.row-header {padding: 0 10px;border-bottom: 1px solid #ccc;}}*/
}
tr {height : 16px; padding : 2px;}
td {width : 16px; min-width :16px;}
table {font-size:12px;}
table.t {position: absolute;left: 30px;font-size:11px;  white-space: nowrap;}
div.a {width:130px; height:12px; white-space: nowrap; font-size: 12px; text-align: left; /* background-color: #b0c4de;*/ font-family: Arial, Helvetica, sans-serif;
          -webkit-transform:rotate(-50deg); /* for Safari and Chrome */
          -ms-transform:rotate(-50deg); /* this for oldish IE*/
          -moz-transform:rotate(-50deg); /* for Firefox */
          -o-transform:rotate(-50deg); /* for Opera */
}
div.b {border: 1px solid #a1a1a1; padding: 2px 2px; background: #0000ff;
    width: 15px; height : 15px; border-radius: 3px;}

div.c {padding: 2px 2px; width: 80px; height: 15px; padding-top: 4px}

div.d {font-size:10px;}

div.grey{border: 1px solid #a1a1a1; padding: 2px 2px; background: #d3d3d3;
    width: 15px; height : 15px; border-radius: 3px;}
</style>
<script>
function c(x) {var res = x.id.split("-");document.getElementById(res[1]).style.background = "#33cc66"; }
function d(x) {var res = x.id.split("-");document.getElementById(res[1]).style.background = ""; }
</script>
</head>
<body> 
'''

footer = '''
</body>
</html>
'''
