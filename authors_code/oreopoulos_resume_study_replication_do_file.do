
use "oreopoulos resume study replication data file temp.dta", clear


*********************************************
* statistics and descriptive sample sizes
*********************************************

table name type, by(name_ethnicity female)
table name type, by(name_ethnicity female) c(sum callback)

gen canada = name_ethnicity=="Canada"

#delimit ;
table type, c(
mean female 
mean ba_quality 
mean extracurricular_skills 
mean language_skills
mean ma
) row
;

#delimit ;
table type, c(
mean same_exp
mean exp_highquality
mean reference
mean legal
mean accreditation
) row
;
#delimit cr

#delimite ;
gen greek = name_ethn=="Greek"
gen chinese_english = name_ethn=="Chn-Cdn"
#delimit ;
table type, c(
mean canada
mean chinese
mean pakistani
mean indian
mean british
) row
;

#delimit cr


**********************
*table 4
**********************
drop if accreditation==1 | reference==1 | legal==1
xi: reg callback i.type i.fall_data if name_ethnicity=="Indian" | name_ethnicity=="Canada", robust
outreg2 _Itype* using tables, replace bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type i.fall_data if name_ethnicity=="Pakistani" | name_ethnicity=="Canada", robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type i.fall_data if name_ethnicity=="Chinese" | name_ethnicity=="Canada", robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type i.fall_data if name_ethnicity=="Chn-Cdn" | name_ethnicity=="Canada", robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type i.fall_data if name_ethnicity=="British" | name_ethnicity=="Canada", robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type i.fall_data if name_ethnicity=="Greek" | name_ethnicity=="Canada", robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type i.fall_data if name_ethnicity=="Indian" | name_ethnicity=="Chinese" | name_ethnicity=="Pakistani" | name_ethnicity=="Canada", robust
outreg2 _Itype* using tables, append bdec(3) aster(se) seeo excel bracket(se)


*******************************************************************************************
* drop british sample, sample with canadian-chinese, and greek names for rest of analysis
*******************************************************************************************
drop if name_ethnicity=="British" | name_ethnicity=="Chn-Cdn" | name_ethnicity=="Greek"


************************
* table 5
************************
replace same_exp=0 if same_exp==.
replace reference = 0 if reference==.
replace accreditation=0 if accreditation==.
replace legal=0 if legal==.
replace extracurricular_skills=0 if extracurricular_skills==.

xi: reg callback i.type i.fall_data, robust
outreg2 _Itype* using tables, replace bdec(3) aster(se) excel bracket(se)
xi: areg callback i.type, robust absorb(firmid)
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal i.fall_data, robust
outreg2 _Itype* female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal using tables, append bdec(3) aster(se) excel bracket(se)
xi: areg callback i.type female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal , robust absorb(firmid)
outreg2 _Itype* female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal using tables, append bdec(3) aster(se) excel bracket(se) seeo

xi: reg callback female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual i.fall_data, robust
outreg2 female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual using tables, replace bdec(3) aster(se) excel bracket(se)
xi: reg callback female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual i.fall_data if type==0, robust
outreg2 female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal i.fall_data if type==1, robust
outreg2 female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal i.fall_data if type==2, robust
outreg2 female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal i.fall_data if type==3, robust
outreg2 female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal using tables, append bdec(3) aster(se) excel bracket(se)
xi: reg callback female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal i.fall_data if type==4, robust
outreg2 female ba_quality extracurricular_skills language_skills ma same_exp exp_highqual reference accreditation legal using tables, append bdec(3) aster(se) excel bracket(se) seeo


**************************
* table 6
**************************
replace skillspeaking=skillspeaking/100
replace skillsocialper=skillsocialper/100
replace skillwriting=skillwriting/100

replace skillspeaking = skillspeaking+skillsocialper+skillwriting


egen p10 = pctile(skillspeaking), p(10)
egen p20 = pctile(skillspeaking), p(20)
egen p30 = pctile(skillspeaking), p(30)
egen p40 = pctile(skillspeaking), p(40)
egen p50 = pctile(skillspeaking), p(50)
egen p60 = pctile(skillspeaking), p(60)
egen p70 = pctile(skillspeaking), p(70)
egen p80 = pctile(skillspeaking), p(80)
egen p90 = pctile(skillspeaking), p(90)

xi: reg callback i.type i.fall if skillspeakin<=p10 & skillspeakin~=., robust
outreg2 _Itype* using tables, replace bdec(3) aster(se) excel bracket(se)
xi: reg callback i.type i.fall if skillspeakin>=p10 & skillspeakin<=p20, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p20 & skillspeakin<=p30, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p30 & skillspeakin<=p40, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p40 & skillspeakin<=p50, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p50 & skillspeakin<=p60, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p60 & skillspeakin<=p70, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p70 & skillspeakin<=p80, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p80 & skillspeakin<=p90, robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) 
xi: reg callback i.type i.fall if skillspeakin>=p90 & skillspeakin~=., robust
outreg2 _Itype* using tables, append bdec(3) aster(se) excel bracket(se) seeo





