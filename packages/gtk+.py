class GtkPackage (GnomeGitPackage):
	def __init__ (self):
		GnomeGitPackage.__init__ (self, 'gtk+', '2.24', 'e62709da2ee6619f26c8446b545418e5f1b9e151',
			configure_flags = [
				'--with-gdktarget=%{gdk_target}',
#				'--disable-cups',
			]
		)
		self.gdk_target = 'x11'

		if Package.profile.name == 'darwin':
			self.gdk_target = 'quartz'
			self.sources.extend ([
				# Custom gtkrc
				'patches/gtkrc',

				# smooth scrolling, scrollbars, overscroll, retina, gtknsview
				'patches/gtk/0001-Add-gdk_screen_get_monitor_workarea-and-use-it-all-o.patch',
				'patches/gtk/0002-gtk-don-t-scroll-combo-box-menus-if-less-than-3-item.patch',
				'patches/gtk/0003-gtk-paint-only-the-exposed-region-in-gdk_window_expo.patch',
				'patches/gtk/0004-Implement-gtk-enable-overlay-scrollbars-GtkSetting.patch',
				'patches/gtk/0005-Smooth-scrolling.patch',
				'patches/gtk/0006-gtk-Add-a-way-to-do-event-capture.patch',
				'patches/gtk/0007-gtk-don-t-let-insensitive-children-eat-scroll-events.patch',
				'patches/gtk/0008-scrolledwindow-Kinetic-scrolling-support.patch',
				'patches/gtk/0009-gtk-paint-to-the-right-windows-in-gtk_scrolled_windo.patch',
				'patches/gtk/0010-GtkScrolledWindow-add-overlay-scrollbars.patch',
				'patches/gtk/0011-gtk-add-event-handling-to-GtkScrolledWindow-s-overla.patch',
				'patches/gtk/0012-Use-gtk-enable-overlay-scrollbars-in-GtkScrolledWind.patch',
				'patches/gtk/0013-gtk-correctly-handle-toggling-of-the-scrollbar-visib.patch',
				'patches/gtk/0014-gtk-handle-gtk-primary-button-warps-slider-for-the-o.patch',
				'patches/gtk/0015-Introduce-phase-field-in-GdkEventScroll.patch',
				'patches/gtk/0016-Add-hack-to-lock-flow-of-scroll-events-to-window-whe.patch',
				'patches/gtk/0017-Introduce-a-background-window.patch',
				'patches/gtk/0018-Make-scrolled-window-work-well-with-Mac-touchpad.patch',
				'patches/gtk/0019-Use-start-end-phase-in-event-handling.patch',
				'patches/gtk/0020-Improve-overshooting-behavior.patch',
				'patches/gtk/0021-Cancel-out-smaller-delta-component.patch',
				'patches/gtk/0022-quartz-Add-a-dummy-NSView-serving-as-layer-view.patch',
				'patches/gtk/0023-gtk-port-overlay-scrollbars-to-native-CALayers.patch',
				'patches/gtk/0024-Refrain-from-starting-fading-out-while-a-gesture-is-.patch',
				'patches/gtk/0025-gtk-don-t-show-the-olverlay-scrollbars-if-only-the-s.patch',
				'patches/gtk/0026-Reclamp-unclamped-adjustments-after-resize.patch',
				'patches/gtk/0027-gtk-fix-size_request-of-scrolled-window.patch',
				'patches/gtk/0028-Hackish-fix-for-bug-8493-Min-size-of-GtkScrolledWind.patch',
				'patches/gtk/0029-Add-momentum_phase-to-GdkEventScroll.patch',
				'patches/gtk/0030-Never-intervene-in-the-event-stream-for-legacy-mice.patch',
				'patches/gtk/0031-Do-not-start-overshooting-for-legacy-mouse-scroll-ev.patch',
				'patches/gtk/0032-gtk-remove-the-overlay-scrollbar-grab-on-unrealize.patch',
				'patches/gtk/0033-gtk-add-GtkScrolledWindow-API-to-disable-overshoot-p.patch',
				'patches/gtk/0034-quartz-return-events-on-embedded-foreign-NSViews-bac.patch',
				'patches/gtk/0035-quartz-don-t-forward-events-to-the-toplevel-nswindow.patch',
				'patches/gtk/0036-gdk-add-a-move-native-children-signal-to-GdkWindow.patch',
				'patches/gtk/0037-gtk-add-new-widget-GtkNSView-which-alows-to-embed-an.patch',
				'patches/gtk/0038-tests-add-a-notebook-to-testnsview.c.patch',
				'patches/gtk/0039-gtk-connect-GtkNSView-to-move-native-children-and-re.patch',
				'patches/gtk/0040-tests-add-a-scrolled-window-test-widget-to-testnsvie.patch',
				'patches/gtk/0041-gtknsview-clip-drawRect-to-a-parent-GtkViewport-s-wi.patch',
				'patches/gtk/0042-gtk-clip-NSViews-to-the-scrolled-window-s-overshoot_.patch',
				'patches/gtk/0043-gtk-implement-clipping-to-multiple-parent-viewports-.patch',
				'patches/gtk/0044-gtk-first-attempt-to-also-clip-NSWindow-s-field-edit.patch',
				'patches/gtk/0045-gtk-also-clip-the-NSView-s-subviews.patch',
				'patches/gtk/0046-nsview-also-swizzle-DidAddSubview-and-clip-all-subvi.patch',
				'patches/gtk/0047-nsview-clip-text-field-cursor-drawing.patch',
				'patches/gtk/0048-nsview-factor-out-almost-all-code-from-the-overridde.patch',
				'patches/gtk/0049-gtk-add-an-overlay-policy-API-to-GtkScrolledWindow.patch',
				'patches/gtk/0050-quartz-add-gdk_screen_-and-gdk_window_get_scale_fact.patch',
				'patches/gtk/0051-gtk-add-gtk_widget_get_scale_factor.patch',
				'patches/gtk/0052-iconfactory-Add-_scaled-variants.patch',
				'patches/gtk/0053-widget-Add-_scaled-variants-for-icon-rendering.patch',
				'patches/gtk/0054-icontheme-Add-support-for-high-resolution-icons.patch',
				'patches/gtk/0055-iconfactory-Add-scale-info-to-GtkIconSource.patch',
				'patches/gtk/0056-iconfactory-Add-gtk_cairo_set_source_icon_set.patch',
				'patches/gtk/0057-image-Use-scaled-icons-on-windows-with-a-scaling-fac.patch',
				'patches/gtk/0058-cellrendererpixbuf-Use-scaled-icons-on-windows-with-.patch',
				'patches/gtk/0059-entry-Use-scaled-icons-on-windows-with-a-scale-facto.patch',
				'patches/gtk/0060-gdk-Lookup-double-scaled-variants-on-pixbufs.patch',
				'patches/gtk/0061-Make-usual-calls-to-get-a-GdkPixbuf-attach-a-2x-vari.patch',
				'patches/gtk/retina-CellRendererPixbuf.patch',

				'patches/gtk/fix-icon-criticals.patch',

				# Bug 12765 - GtkNSView keyboard input not propagated through non-acceptsFirstResponder NSView
				# https://bugzilla.xamarin.com/show_bug.cgi?id=12765
				'patches/gtk/GtkNSView-keyinput.patch',

				# Bug 702841 - GdkQuartz does not distinguish Eisu, Kana and Space keys on Japanese keyrboard
				# https://bugzilla.gnome.org/show_bug.cgi?id=702841
				'patches/gtk/bgo702841-fix-kana-eisu-keys.patch',

				# make new modifier behviour opt-in, so as not to break old versions of MonoDevelop
				'patches/gdk-quartz-set-fix-modifiers-hack-v3.patch',

				# attempt to work around 2158 - [GTK] crash triggering context menu
				# also prints some warnings that may help to debug the real issue
				# https://bugzilla.xamarin.com/attachment.cgi?id=1644
				'patches/gtk/bxc2158_workaround_crash_triggering_context_menu.patch',

				# Zoom, rotate, swipe events
				'patches/gtk-gestures.patch',

				# Fix gtk_window_begin_move_drag on Quartz
				'patches/gtk-quartz-move-drag.patch',

				# Bug 6156 - [gtk] Quitting the application with unsaved file and answering Cancel results in crash
				# https://bugzilla.xamarin.com/attachment.cgi?id=2214
				'patches/gtk/bxc6156_quit_with_unsaved_file_and_cancel_results_in_crash.patch',

				# Bug 3457 - [GTK] Support more standard keyboard shortcuts in dialogs
				# https://bugzilla.xamarin.com/attachment.cgi?id=2240
				'patches/gtk/bxc3457_more_standard_keyboard_shortcuts.patch',

				# Bug  10256 - Mac window manipulation tools get confused by Xamarin Studio
				# https://bugzilla.xamarin.com/attachment.cgi?id=3465
				'patches/gtk/bxc_10256_window_tools_get_confused.diff',
				
				'patches/gtk/0001-Implement-IME-reset-for-imquartz.patch',
			])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (2, len (self.sources)):
				self.sh ('patch -p1 --ignore-whitespace < "%{sources[' + str (p) + ']}"')

	def install(self):
		Package.install(self)
		if Package.profile.name == 'darwin':
			self.install_gtkrc ()

	def install_gtkrc(self):
		gtkrc = self.sources[1]
		origin = gtkrc if os.path.isabs (gtkrc) else os.path.join (self.package_dir (), gtkrc)
		destdir = os.path.join (self.prefix, "etc", "gtk-2.0")
		if not os.path.exists (destdir):
			os.makedirs(destdir)
		self.sh('cp %s %s' % (origin, destdir))

GtkPackage ()
