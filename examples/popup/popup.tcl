#############################################################################
# Generated by PAGE version 7.6g
#  in conjunction with Tcl version 8.6
#  Nov 02, 2022 09:14:05 AM PDT  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 14"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set vTcl(actual_gui_font_tooltip_desc)  TkTooltipFont
set vTcl(actual_gui_font_tooltip_name)  TkTooltipFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #f4bcb2
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) wheat
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top36 {base} {
    global vTcl
    if {$base == ""} {
        set base .top36
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m44" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+751+195
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "New Toplevel 1"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    button "$top.but37" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Button1 
    vTcl:DefineAlias "$top.but37" "Button1" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but37 <Button-3> {
        lambda e: popup1(e)
    }
    button "$top.but38" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Button2 
    vTcl:DefineAlias "$top.but38" "Button2" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but38 <Button-3> {
        lambda e: popup2(e)
    }
#### Spot menu dumpCmd A
    menu "$top.m44" \
        -activebackground #d8d8d8 -activeforeground #000000 \
        -background $vTcl(actual_gui_menu_bg) \
        -font $vTcl(actual_gui_font_menu_desc) \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
#### Spot menu dumpCmd B
    $top.m44 add command \
        -command {#quit} -label Quit 
    vTcl::widgets::core::popup::createCmd "$top.pop50" \
        -activebackground #ffffcd -activeforeground black -background #dda0dd \
        -disabledforeground #b8a786 -font TkMenuFont -foreground black \
        -tearoff 1 
    global vTcl
    set val vTcl($top.pop50,-proc)
    set vTcl($top.pop50,-proc) popup1
    namespace eval ::widgets::$top.pop50 {}
    set ::widgets::$top.pop50::ClassOption(-proc) popup1
    set ::widgets::$top.pop50::options(-proc) popup1
    set ::widgets::$top.pop50::save(-proc) 1
    vTcl:DefineAlias "$top.pop50" "Popup1" vTcl:WidgetProc "" 1
    $top.pop50 add command \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_bg) \
        -command this \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label This 
    $top.pop50 add command \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_bg) \
        -command that \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label That 
    $top.pop50 add separator \
        -background $vTcl(actual_gui_bg) 
    $top.pop50 add cascade \
        -menu "$top.mnu48" -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #111111 -background $vTcl(actual_gui_bg) \
        -command {{}} \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label Also 
    set site_3_0 $top.pop50
    menu "$top.mnu48" \
        -activeforeground black -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground black -tearoff 0 
    $top.mnu48 add command \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_bg) \
        -command then \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label Then 
    $top.mnu48 add command \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_bg) \
        -command there \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label There 
    vTcl::widgets::core::popup::createCmd "$top.pop53" \
        -activebackground #ffffcd -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font TkMenuFont -foreground black -tearoff 1 
    global vTcl
    set val vTcl($top.pop53,-proc)
    set vTcl($top.pop53,-proc) popup2
    namespace eval ::widgets::$top.pop53 {}
    set ::widgets::$top.pop53::ClassOption(-proc) popup2
    set ::widgets::$top.pop53::options(-proc) popup2
    set ::widgets::$top.pop53::save(-proc) 1
    vTcl:DefineAlias "$top.pop53" "Popup2" vTcl:WidgetProc "" 1
    $top.pop53 add command \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background plum -command how \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label How 
    $top.pop53 add command \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background plum -command now \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label Now 
    $top.pop53 add separator \
        -background plum 
    $top.pop53 add cascade \
        -menu "$top.mnu51" -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #111111 -background plum \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label BrownCow 
    set site_3_0 $top.pop53
    menu "$top.mnu51" \
        -activeforeground black -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground black -tearoff 0 
    $top.mnu51 add command \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background plum -command moo \
        -font {-family {DejaVu Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_menu_fg) -label Moo 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but37 \
        -in $top -x 140 -y 170 -anchor nw -bordermode ignore 
    place $top.but38 \
        -in $top -x 410 -y 170 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top36 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

