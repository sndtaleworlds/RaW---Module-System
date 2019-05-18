This kit includes all files necessary for ModMerger to install PBOD and motomataru's formations,
Include the resources and textures with your module and make sure that you edit your module.ini 
to load the resources noted in the included module.ini

Copy all of the .py files into your module system folder.

If you have used a prior version of modmerger, you may need to overwrite some of your util_* files as 
PBOD uses custom utilities created for sphere's modmerger system by Caba'drin.

To compile your module:
First, this requires a 'mostly' Native module_mission_templates (it can deal with nearly any kind of
edit to any other file) for battle continuation to function appropriately. If you have concerns about this,
contant Caba'drin via the Taleworlds forums.

Second, run "modmerger_installer" (see the modmerger_readme for more on this) to wrap your module_* files.
Third, check the *_constants files for any possible slot conflicts (formAI_constants, formations_constants
and pbod_constants againts your module_constants).

Fourth, compile the module as normal. The PBOD and Formations code will be added automatically.