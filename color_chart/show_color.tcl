#############################################################################
# Generated by PAGE version 8.0N
#  in conjunction with Tcl version 8.6
#  Dec 10, 2023 08:47:06 AM PST  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 12"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {Nimbus Sans L} -size 14"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #f4bcb2
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
set vTcl(project_theme) page-legacy



proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
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
        -background wheat -highlightbackground wheat 
    wm focusmodel $top passive
    wm geometry $top 397x337+733+169
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Show Color"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    label "$top.lab46" \
        -activebackground #ffffcd -activeforeground black -background wheat \
        -compound left -disabledforeground #b8a786 \
        -font "-family {DejaVu Sans} -size 14 -weight bold" \
        -foreground #000000 -highlightbackground wheat -text "Label" 
    vTcl:DefineAlias "$top.lab46" "Label1" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes47" \
        -background wheat -font "-family {DejaVu Sans} -size 13 -weight bold" \
        -foreground #000000 -highlightbackground wheat -padx 1 -pady 1 \
        -text "Message" -width 90 
    vTcl:DefineAlias "$top.mes47" "Message2" vTcl:WidgetProc "Toplevel1" 1
    frame "$top.fra48" \
        -borderwidth 2 -relief groove -background wheat -height 75 \
        -highlightbackground wheat -width 125 
    vTcl:DefineAlias "$top.fra48" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes48" \
        -background wheat -font "-family {DejaVu Sans} -size 13 -weight bold" \
        -foreground #000000 -highlightbackground wheat \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Message" -width 90 
    vTcl:DefineAlias "$top.mes48" "Message2_1" vTcl:WidgetProc "Toplevel1" 1
    frame "$top.fra49" \
        -borderwidth 2 -relief groove -background wheat -height 75 \
        -highlightbackground wheat -highlightcolor #000000 -width 125 
    vTcl:DefineAlias "$top.fra49" "Frame1_1" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes50" \
        -background wheat -font "-family {DejaVu Sans} -size 13 -weight bold" \
        -foreground #000000 -highlightbackground wheat \
        -highlightcolor #000000 -padx 1 -pady 1 -text "Message" -width 90 
    vTcl:DefineAlias "$top.mes50" "Message3_1" vTcl:WidgetProc "Toplevel1" 1
    button "$top.but50" \
        -activebackground beige -activeforeground black -background wheat \
        -borderwidth 2 -command "sys.exit" -compound left \
        -disabledforeground #b8a786 \
        -font "-family {DejaVu Sans} -size 12 -weight bold" \
        -foreground #000000 -highlightbackground wheat -text "Quit" 
    vTcl:DefineAlias "$top.but50" "Button1" vTcl:WidgetProc "Toplevel1" 1
    message "$top.mes49" \
        -background wheat -font "-family {DejaVu Sans} -size 13 -weight bold" \
        -foreground #000000 -highlightbackground wheat -padx 1 -pady 1 \
        -text "Message" -width 90 
    vTcl:DefineAlias "$top.mes49" "Message3" vTcl:WidgetProc "Toplevel1" 1
    label "$top.lab47" \
        -activebackground #ffffcd -activeforeground black -background wheat \
        -compound left -disabledforeground #b8a786 \
        -font "-family {DejaVu Sans} -size 14 -weight bold" \
        -foreground #000000 -highlightbackground wheat \
        -highlightcolor #000000 -text "Label" 
    vTcl:DefineAlias "$top.lab47" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label "$top.lab48" \
        -activeforeground #000000 -anchor w -background wheat -compound left \
        -disabledforeground #b8a786 \
        -font "-family {DejaVu Sans} -size 14 -weight bold" \
        -foreground #000000 -text "Color" 
    vTcl:DefineAlias "$top.lab48" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label "$top.lab49" \
        -activeforeground #000000 -anchor w -background wheat -compound left \
        -disabledforeground #b8a786 \
        -font "-family {DejaVu Sans} -size 14 -weight bold" \
        -foreground #000000 -text "Complement" 
    vTcl:DefineAlias "$top.lab49" "Label3" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab46 \
        -in $top -x 30 -y 70 -width 151 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes47 \
        -in $top -x 60 -y 110 -anchor nw -bordermode ignore 
    place $top.fra48 \
        -in $top -x 40 -y 150 -anchor nw -bordermode ignore 
    place $top.mes48 \
        -in $top -x 230 -y 110 -width 89 -relwidth 0 -height 26 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra49 \
        -in $top -x 210 -y 150 -width 125 -relwidth 0 -height 75 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes50 \
        -in $top -x 230 -y 230 -width 89 -relwidth 0 -height 26 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 160 -y 280 -anchor nw -bordermode ignore 
    place $top.mes49 \
        -in $top -x 60 -y 230 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 200 -y 70 -width 151 -height 27 -anchor nw \
        -bordermode ignore 
    place $top.lab48 \
        -in $top -x 77 -y 30 -width 59 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 215 -y 30 -width 136 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 

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
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

