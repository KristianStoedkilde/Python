from pymol import cmd

acidic_aa = ['ASP','GLU']
basic_aa = ['HIS','LYS','ARG']
aromatic_aa = ['PHE','TRP','TYR',"HIS"]

#Colors
acid_color = "tv_red"
base_color = "marine"
aromatic_color = "limon"

' type of color:'
'                acid'
'                base'
'                aromatic'

def color_by_res_type(type_of_color):

	stored.list=[]
	cmd.iterate("(name ca)","stored.list.append((resi,resn))") 
  
	for i in range(len(stored.list)):

		if ((stored.list[i][1]) in acidic_aa) and (type_of_color == "acid"):
			cmd.color(acid_color,"resi %s" % (stored.list[i][0]))
		elif ((stored.list[i][1]) in basic_aa) and (type_of_color == "base"):
			cmd.color(base_color,"resi %s" % (stored.list[i][0]))
		elif ((stored.list[i][1]) in aromatic_aa) and  (type_of_color == "aromatic"):	
			print (stored.list[i][1] + " " + str(i))

			cmd.color(aromatic_color,"resi %s" % (stored.list[i][0])) 

cmd.extend("color_by_res_type", color_by_res_type)