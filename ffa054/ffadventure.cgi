#!/usr/local/bin/perl

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'ffadventure.ini';



#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if($mente) { &error("���݃����e�i���X���ł��B���΂炭���҂����������B"); }
&decode;
&max_strings;

if($mode eq "") { &html_top; }
elsif($mode eq 'log_in') { &log_in; }
elsif($mode eq 'chara_make') { &chara_make; }
elsif($mode eq 'make_end') { &make_end; }
elsif($mode eq 'regist') { &regist; }
elsif($mode eq 'battle') { &battle; }
elsif($mode eq 'tensyoku') { &tensyoku; }
elsif($mode eq 'monster') { &monster; }
elsif($mode eq 'ranking') { &ranking; }
elsif($mode eq 'yado') { &yado; }
elsif($mode eq 'message') { &message; }
elsif($mode eq 'item_shop') { &item_shop; }
elsif($mode eq 'item_buy') { &item_buy; }
&html_top;
#------------#
#  �퓬���  #
#------------#
sub battle {

	open(IN,"<$chara_file");
	@battle = <IN>;
	close(IN);

	foreach(@battle){
		($kid,$kpass,$ksite,$kurl,$kname,$ksex,$kchara,$kn_0,$kn_1,$kn_2,$kn_3,$kn_4,$kn_5,$kn_6,$ksyoku,$kclass,$khp,$kmaxhp,$kex,$klv,$kgold,$klp,$ktotal,$kkati,$kwaza,$ki_name,$ki_dmg,$kmons,$khost,$kdate) = split(/<>/);
		if($in{'id'} eq "$kid") { last; }
	}
	if (($in{'id'} ne $kid) or ($in{'pass'} ne $kpass)) {&error('ID�A�p�X���[�h���Ⴂ�܂�');}

	$ltime = time();
	$ltime = $ltime - $kdate;
	$vtime = $b_time - $ltime;
	$mtime = $m_time - $ltime;
	if($in{'id'} ne "$kid") {&error("�I�[�v���G���[�AID�E�p�X���[�h������������܂���B");}

	if($ltime < $b_time and $ktotal) {
		&error("$vtime�b�㓬����悤�ɂȂ�܂��B\n");
	}

	&read_winner;

	if($wid eq $kid) { &error("���݃`�����v�Ȃ̂œ����܂���B"); }

	if($chanp_milit) {
		if($kurl eq $lurl) { &error("�`�����v���ς��܂œ����܂���B"); }
	}

	if($in{'site'}) { $ksite = $in{'site'}; }
	if($in{'url'}) { $kurl = $in{'url'}; }
	if($in{'waza'}) { $kwaza = $in{'waza'}; }
	if($in{'c_name'}) { $kname = $in{'c_name'}; }
	$khp_flg = $khp;
	$whp_flg = $whp;

	$i=1;$j=0;@battle_date=();
	foreach(1..$turn) {
		$dmg1 = $klv * (int(rand(3)) + 1);
		$dmg2 = $wlv * (int(rand(3)) + 1);
		$clit1 = "";
		$clit2 = "";
		$com1 = "";
		$com2 = "";
		$kawasi1 = "";
		$kawasi2 = "";

		$hissatu_c = -1;

			# ����҃_���[�W�v�Z
				if($ki_name) { $com1 = "$kname��$ki_name�ōU���I�I<p>"; }
				else { $com1 = "$kname�̍U���I�I<p>"; }
			if($ksyoku == 0){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 0;
					$dmg1 = $dmg1 * 5;
				}
				$dmg1 = $dmg1 + int(rand($kn_0)) + $ki_dmg;
			}elsif($ksyoku == 1){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 1;
					$dmg1 = $dmg1 * 5;
				}
				$dmg1 = $dmg1 + int(rand($kn_1)) + $ki_dmg;
			}elsif($ksyoku == 2){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 2;
					$dmg1 = $dmg1 * 5;
				}
				$dmg1 = $dmg1 + int(rand($kn_2)) + $ki_dmg;
			}elsif($ksyoku == 3){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 3;
					$dmg1 = $dmg1 * 5;
				}
				$dmg1 = $dmg1 + int(rand($kn_3)) + $ki_dmg;
			}elsif($ksyoku == 4){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 4;
					$dmg1 = $dmg1 * 5;
				}
				$dmg1 = $dmg1 + int(rand($kn_3)) + int(rand($kn_0)) + $ki_dmg;
			}elsif($ksyoku == 5){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 5;
					$dmg1 = $dmg1 * 6;
				}
				$dmg1 = $dmg1 + (int(rand($kn_1)) + int(rand($kn_4))) + $ki_dmg;
			}elsif($ksyoku == 6){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 6;
					$dmg1 = $dmg1 * 6;
				}
				$dmg1 = $dmg1 + (int(rand($kn_1)) + int(rand($kn_4))) + $ki_dmg;
			}elsif($ksyoku == 7){
				if(0 == int(rand(7))) {
					$hissatu_c = 7;
					$dmg1 = $dmg1 * 6;
				}
				$dmg1 = $dmg1 + (int(rand($kn_1)) + int(rand($kn_3))) + $ki_dmg;
			}elsif($ksyoku == 9){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 8;
					$dmg1 = $dmg1 * 8;
				}
				$dmg1 = $dmg1 * (int(rand($kn_1)) + int(rand($kn_2))) + $ki_dmg;
			}elsif($ksyoku == 8){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 9;
					$dmg1 = $dmg1 * 8;
				}
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2)) + $ki_dmg;
			}elsif($ksyoku == 10){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 10;
					$dmg1 = $dmg1 * 9;
				}
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2)) + $ki_dmg;
			}elsif($ksyoku == 11){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 11;
					$dmg1 = $dmg1 * 9;
				}
				$dmg1 = $dmg1 + int(rand($kn_4)) + int(rand($kn_5)) + $ki_dmg;
			}elsif($ksyoku == 12){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 12;
					$dmg1 = $dmg1 * 9;
				}
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2)) + $ki_dmg;
			}elsif($ksyoku == 13){
				if(0 == int(rand($waza_ritu))) {
					$hissatu_c = 13;
					$dmg1 = $dmg1 * 9;
				}
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2)) + $ki_dmg;
			}
			if ($hissatu_c >= 0 ) { # �ύX�𔻒�B
				$com1 .= "<font size=5>$kname�u<b>$kwaza</b>�v</font><p><font color=\"#CC6699\" size=5><b>$hissatu[$hissatu_c]</b></font>\n";
			}

			# �`�����v�_���[�W�v�Z

		if($wi_name){ $com2 = "$wname�́A$wi_name�ōU���I�I"; }
		else{ $com2 = "$wname�̍U���I�I<p>"; }
			if($wsyoku == 0){
				$dmg2 = $dmg2 + int(rand($wn_0)) + $wi_dmg;
			}elsif($wsyoku == 1){
				$dmg2 = $dmg2 + int(rand($wn_1)) + $wi_dmg;
			}elsif($wsyoku == 2){
				$dmg2 = $dmg2 + int(rand($wn_2)) + $wi_dmg;
			}elsif($wsyoku == 3){
				$dmg2 = $dmg2 + int(rand($wn_4)) + $wi_dmg;
			}elsif($wsyoku == 4){
				$dmg2 = $dmg2 + int(rand($wn_3)) + int(rand($wn_0)) + $wi_dmg;
			}elsif($wsyoku == 5){
				$dmg2 = $dmg2 + (int(rand($wn_1)) + int(rand($wn_4))) + $wi_dmg;
			}elsif($wsyoku == 6){
				$dmg2 = $dmg2 + int(rand($wn_1)) + int(rand($wn_4)) + $wi_dmg;
			}elsif($wsyoku == 7){
				$dmg2 = $dmg2 + (int(rand($wn_1)) + int(rand($wn_3))) + $wi_dmg;
			}elsif($wsyoku == 8){
				$dmg2 = $dmg2 + (int(rand($wn_1)) + int(rand($wn_2))) + $wi_dmg;
			}elsif($wsyoku == 9){
				$dmg2 = $dmg2 + int(rand($wn_0)) + int(rand($wn_2)) + $wi_dmg;
			}elsif($wsyoku == 10){
				$dmg2 = $dmg2 + int(rand($wn_0)) + int(rand($wn_2)) + $wi_dmg;
			}elsif($wsyoku == 11){
				$dmg2 = $dmg2 + int(rand($wn_4)) + int(rand($wn_5)) + $wi_dmg;
			}elsif($wsyoku == 12){
				$dmg2 = $dmg2 + int(rand($wn_0)) + int(rand($wn_2)) + $wi_dmg;
			}elsif($wsyoku == 13){
				$dmg2 = $dmg2 + int(rand($wn_0)) + int(rand($wn_2)) + $wi_dmg;
			}

			if(int(rand(20)) == 0) {
				$clit1 = "<b class=\"clit\">�N���e�B�J���I�I</b>";
				$dmg1 = $dmg1 * 2;
			}

			if(int(rand(30)) == 0) {
				$clit2 = "<font size=5>$wname�u<b>$wwaza</b>�v</font><p><b class=\"clit\">�N���e�B�J���I�I</b>";
				$dmg2 = int($dmg2 * 1.5);
			}

			if(($wlv - $klv) >= $level_sa and $i == 1) {
				$sa = $wlv - $klv;
				$clit1 .= "<p><font size=5><b>$kname�̑̂�������̂悤�Ȃ��̂��N���オ��E�E�E�B</b></font>";
				$dmg1 = $dmg1 + $kmaxhp;
			}

		$battle_date[$j] = <<"EOM";
<TABLE BORDER=0>
<TR>
	<TD CLASS="b2" COLSPAN="3" ALIGN="center">
	$i�^�[��
	</TD>
</TR>
<TR>
	<TD ALIGN="center">
	<IMG SRC="$img_path/$chara_img[$kchara]">
	</TD>
	<TD>
	</TD>
	<TD ALIGN="center">
	<IMG SRC="$img_path/$chara_img[$wchara]">
	</TR>
<TR>
<TD>
<TABLE BORDER=1>
<TR>
	<TD CLASS="b1">
	�Ȃ܂�
	</TD>
	<TD CLASS="b1">
	HP
	</TD>
	<TD CLASS="b1">
	�E��
	</TD>
	<TD CLASS="b1">
	LV
	</TD>
</TR>
<TR>
	<TD>
	$kname
	</TD>
	<TD>
	$khp_flg\/$kmaxhp
	</TD>
	<TD>
	$chara_syoku[$ksyoku]
	</TD>
	<TD>
	$klv
	</TD>
</TR>
</TABLE>
</TD>
<TD>
<FONT SIZE=5 COLOR="#9999DD">VS</FONT>
</TD>
<TD>
<TABLE BORDER=1>
<TR>
	<TD CLASS="b1">
	�Ȃ܂�
	</TD>
	<TD CLASS="b1">
	HP
	</TD>
	<TD CLASS="b1">
	�E��
	</TD>
	<TD CLASS="b1">
	LV
	</TD>
</TR>
<TR>
	<TD>
	$wname
	</TD>
	<TD>
	$whp_flg\/$wmaxhp
	</TD>
	<TD>
	$chara_syoku[$wsyoku]
	</TD>
	<TD>
	$wlv
	</TD>
</TR>
</TABLE>
</TD>
</TR>
</TABLE>
<p>
$com1 $clit1 $kawasi2 $wname �� <font class="dmg"><b>$dmg1</b></font> �̃_���[�W��^�����B<p>
$com2 $clit2 $kawasi1 $kname �� <font class="dmg"><b>$dmg2</b></font> �̃_���[�W��^�����B<p>
EOM

		$khp_flg = $khp_flg - $dmg2;
		$whp_flg = $whp_flg - $dmg1;

		if($whp_flg <= 0) { $win = 1; last; }
		elsif($khp_flg <= 0) { $win = 0; last; }

		$i++;
		$j++;
	}

	if($win) {
		$ktotal += 1;
		$kkati += 1;
		$exp = int($wlv * $kiso_exp + (rand($klp) + 1));
		$kex = $kex + $exp;
		$gold = $wlv * 10 + int(rand($klp));
		$kmons = $sentou_limit;
		$comment = "<b><font size=5>$kname�́A�퓬�ɏ��������I�I</font></b><p>";
	}else{
		$ktotal += 1;
		$exp = int($wlv * (rand($klp) + 1));
		$kex = $kex + $exp;
		$gold = int(rand($klp));
		$kmons = $sentou_limit;
		$comment = "<b><font size=5>$kname�́A�퓬�ɕ������E�E�E�B</font></b><p>";
	}

	if($kex >= ($klv * $lv_up)) { &lv_up; }

	$khp = $khp_flg + int(rand($kn_3));
	if($khp > $kmaxhp) { $khp = $kmaxhp; }
	$whp = $whp_flg + int(rand($wn_3));
	if($whp > $wmaxhp) { $whp = $wmaxhp; }
	if($khp <= 0) { $khp = $kmaxhp; }
	if($whp <= 0) { $whp = $wmaxhp; }
	$kgold = $kgold + $gold;

	# �t�@�C�����b�N
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	if($win){
		@new=();
		open(OUT,">$winner_file");
		@winnew = <IN>;
		unshift(@new,"$kid<>$kpass<>$ksite<>$kurl<>$kname<>$ksex<>$kchara<>$kn_0<>$kn_1<>$kn_2<>$kn_3<>$kn_4<>$kn_5<>$kn_6<>$ksyoku<>$kclass<>$khp<>$kmaxhp<>$kex<>$klv<>$kgold<>$klp<>$ktotal<>$kkati<>$kwaza<>$ki_name<>$ki_dmg<>$kmons<>$host<>$date<>$win<>$wsite<>$wurl<>$wname<>\n");
		print OUT @new;
		close(OUT);
	}else{
		$wcount += 1;
		@new=();
		open(OUT,">$winner_file");
		@winnew = <IN>;
		unshift(@new,"$wid<>$wpass<>$wsite<>$wurl<>$wname<>$wsex<>$wchara<>$wn_0<>$wn_1<>$wn_2<>$wn_3<>$wn_4<>$wn_5<>$wn_6<>$wsyoku<>$wclass<>$whp<>$wmaxhp<>$wex<>$wlv<>$wgold<>$wlp<>$wtotal<>$wkati<>$wwaza<>$wi_name<>$wi_dmg<>$wmons<>$host<>$date<>$wcount<>$ksite<>$kurl<>$kname<>\n");
		print OUT @new;
		close(OUT);

		open(IN,"<$recode_file");
		@recode = <IN>;
		close(IN);

		($count,$name) = split(/<>/,$recode[0]);

		if($wcount > $count) {
			open(OUT,">$recode_file");
			print OUT "$wcount<>$wname<>$wsite<>$wurl<>\n";
			close(OUT);
		}
	}

	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	&regist;

	if($refresh and !$win) { &header2; } else { &header; }

	print "<h1>$kname�́A$wname�ɐ킢�𒧂񂾁I�I</h1><hr size=0><p>\n";

	$i=0;
	foreach(@battle_date){
		print "$battle_date[$i]";
		$i++;
	}
	
	print "$comment<p>$kname�́A<b>$exp</b>�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<p>\n";

	&footer;

	exit;
}
#----------------------#
#  �L�����N�^�쐬���  #
#----------------------#
sub chara_make {
	# �w�b�_�[�\��
	&header;

	print <<"EOM";
<h1>�L�����N�^�쐬���</h1>
<hr size=0>
<form action="$script" method="post">
<input type="hidden" name="mode" value="make_end">
<table border=1>
<tr>
<td class="b1">ID</td>
<td><input type="text" name="id" size="10"><br><small>�����D���Ȕ��p�p������4�`8�����ȓ��ł��L�����������B</small></td>
</tr>
<tr>
<td class="b1">�p�X���[�h</td>
<td><input type="password" name="pass" size="10"><br><small>�����D���Ȕ��p�p������4�`8�����ȓ��ł��L�����������B</small></td>
</tr>
<tr>
<td class="b1">�z�[���y�[�W��</td>
<td><input type="text" name="site" size="40"><br><small>�����Ȃ��̃z�[���y�[�W�̖��O�𔼊p$site_maxs�����ȓ��œ��͂��Ă��������B</small></td>
</tr>
<tr>
<td class="b1">URL</td>
<td><input type="text" name="url" size="50" value="http://"><br><small>�����Ȃ��̃z�[���y�[�W�̃A�h���X�𔼊p$url_maxs�����ȓ��ŋL�����Ă��������B</small></td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̖��O</td>
<td><input type="text" name="c_name" size="30"><br><small>���쐬����L�����N�^�[�̖��O�𔼊p$name_maxs�����ȓ��œ��͂��Ă��������B</small></td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̐���</td>
<td><input type="radio" name="sex" value="0">���@<input type="radio" name="sex" value="1">�j<br><small>���쐬����L�����N�^�[�̐��ʂ�I�����Ă��������B</small></td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̃C���[�W</td>
<td><select name="chara">
EOM

	$i=0;
	foreach(@chara_name){
		print "<option value=\"$i\">$chara_name[$i]\n";
		$i++;
	}

	print <<"EOM";
</select><br><small>���쐬����L�����N�^�[�̉摜��I�����Ă��������B(<a href="$chara_list" target="_blank">�摜�ꗗ</a>)</small></td>
</tr>
<tr>
<td class="b1">�L�����N�^�[�̔\\��</td>
<td>
	<table border=1>
	<tr>
	<td class="b2" width="70">��</td><td class="b2" width="70">�m�\\</td><td class="b2" width="70">�M�S</td><td class="b2" width="70">������</td><td class="b2" width="70">��p��</td><td class="b2" width="70">����</td><td class="b2" width="70">����</td>
	</tr>
	<tr>
EOM

	$i=0;$j=0;
	foreach(0..6){
		print "<td>$kiso_nouryoku[$i] + <select name=n_$i>\n";
		foreach(0..10){
			print "<option value=\"$j\">$j\n";
			$j++;
		}
		print "</select>\n";
		print "</td>\n";
		$i++;$j=0;
	}

	print <<"EOM";
	</tr>
	</table>
<small>���{�[�i�X�|�C���g�u<b>10</b>�v�����ꂼ��ɐU�蕪���Ă��������B(�U�蕪�������v��10�ȉ��ɂȂ�悤�ɁB)</small>
</td>
</tr>
<tr>
<td colspan="2" align="center"><input type="submit" value="����œo�^"></td>
</tr>
</table>
</form>
EOM

	# �t�b�^�[�\��
	&footer;

	exit;
}
#----------------#
#  �f�R�[�h����  #
#----------------#
sub decode {
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		if ($ENV{'CONTENT_LENGTH'} > 51200) { &error("���e�ʂ��傫�����܂�"); }
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }
	@pairs = split(/&/, $buffer);
	foreach (@pairs) {
		($name,$value) = split(/=/, $_);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		# �����R�[�h���V�t�gJIS�ϊ�
		&jcode'convert(*value, "sjis", "", "z");

		# �^�O����
		$value =~ s/</&lt;/g;
		$value =~ s/>/&gt;/g;
		$value =~ s/\"/&quot;/g;

		# ���s������
		$value =~ s/\r//g;
		$value =~ s/\n//g;

		$in{$name} = $value;
	}
	$mode = $in{'mode'};
	$in{'url'} =~ s/^http\:\/\///;
	$cookie_pass = $in{'pass'};
	$cookie_id = $in{'id'};
}
#--------------#
#  �G���[����  #
#--------------#
sub error {
	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	&header;
	print "<center><hr width=400><h3>ERROR !</h3>\n";
	print "<P><font color=red><B>$_[0]</B></font>\n";
	print "<P><hr width=400></center>\n";
	print "</body></html>\n";
	exit;
}
#------------------#
#�@HTML�̃t�b�^�[�@#
#------------------#
sub footer {
	if($refresh and !$win and $mode eq 'battle') {
		print "�y<b><a href=\"http\:\/\/$wurl\">�`�����v�̃z�[���y�[�W��</a></b>�z\n";
	}else{
		if($mode ne ""){
			print "<a href=\"$script\">TOP�y�[�W��</a>\n";
		}
		if($kid and $mode ne 'log_in' and $mode ne 'tensyoku' and $mode ne 'yado') { 
			print " / <a href=\"$script?mode=log_in&id=$kid&pass=$kpass\">�X�e�[�^�X��ʂ�</a>\n";
		}
	}
	print "<HR SIZE=0 WIDTH=\"100%\"><DIV align=right class=small>\n";
	print "$ver by <a href=\"http://www.smat.ne.jp/~ffa/index.html\">FFA�J����</a><br>\n";
	print "</DIV>\n";

	if($mode eq 'log_in' and $ltime < $b_time and $ktotal){
	print <<"EOM";
<SCRIPT language="JavaScript">
<!--
window.setTimeout('CountDown()',100);
//-->
</SCRIPT>
EOM
	}
	print "</body></html>\n";
}
#------------------#
#  �N�b�L�[���擾  #
#------------------#
sub get_cookie {
	@pairs = split(/;/, $ENV{'HTTP_COOKIE'});
	foreach (@pairs) {
		local($key,$val) = split(/=/);
		$key =~ s/\s//g;
		$GET{$key} = $val;
	}
	@pairs = split(/\,/, $GET{'FFADV'});
	foreach (@pairs) {
		local($key,$val) = split(/<>/);
		$COOK{$key} = $val;
	}
	$c_id  = $COOK{'id'};
	$c_pass = $COOK{'pass'};
}
#----------------#
#  �z�X�g���擾  #
#----------------#
sub get_host {
	$addr = $ENV{'REMOTE_ADDR'};

	if ($get_remotehost) {
		$host = $ENV{'REMOTE_HOST'};
		if ($host eq "" || $host eq "$addr") {
			$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
		}
	}

	if ($host eq "") { $host = $addr; }
}
#--------------#
#  ���Ԃ��擾  #
#--------------#
sub get_time {
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time);
	@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	# �����̃t�H�[�}�b�g
	$gettime = sprintf("%04d/%02d/%02d %02d:%02d",
			$year+1900,$mon+1,$mday,$hour,$min);
}
#------------------#
#  HTML�̃w�b�_�[  #
#------------------#
sub header {
	print "Cache-Control: no-cache\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html\n\n";
	print <<"EOM";
<html>
<head>
<META name="robots" content="noindex,nofollow">
<META name="robots" content="noarchive">
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
EOM

if($mode eq 'log_in' and $ltime < $b_time and $ktotal){
	print <<"EOM";
<META HTTP-EQUIV="Refresh" CONTENT="$vtime">
<SCRIPT LANGUAGE="JavaScript">
<!--
	var start=new Date();
	start=Date.parse(start)/1000;
	var counts=$vtime;
	function CountDown(){
		var now=new Date();
		now=Date.parse(now)/1000;
		var x=parseInt(counts-(now-start),10);
		if(document.form1){document.form1.clock.value = x;}
		if(x>0){timerID=setTimeout("CountDown()", 100);}
	}
//-->
</SCRIPT>
EOM
}
	print <<"EOM";
<STYLE type="text/css">
<!--
body,tr,td,th { font-size: $b_size }
a:hover { color: $alink }
.small { font-size: 10pt }
.b1 {background: #9ac;border-color: #ccf #669 #669 #ccf;color:#fff; border-style: solid; border-width: 1px;}
.b2 {background: #669;border-color: #99c #336 #336 #99c;color:#fff; border-style: solid; border-width: 1px; text-align: center}
.b3 {background: #fff;border-color: #ccf #669 #669 #ccf;}
.dmg { color: #FF0000; font-size: 18pt }
.clit { color: #0000FF; font-size: 18pt }
-->
</STYLE>
EOM
	print "<title>$main_title</title></head>\n";
	print "<body background=\"$backgif\" bgcolor=\"$bgcolor\" text=\"$text\" link=\"$link\" vlink=\"$vlink\" alink=\"$alink\">\n";
}
#--------------#
#  �������җp  #
#--------------#
sub header2 {
	print "Content-type: text/html\n\n";
	print <<"EOM";
<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META http-equiv="refresh" content="$refresh;URL=http\:\/\/$wurl"> 
<STYLE type="text/css">
<!--
body,tr,td,th { font-size: $b_size }
a:hover { color: $alink }
.small { font-size: 10pt }
.b1 {background: #9ac;border-color: #ccf #669 #669 #ccf;color:#fff; border-style: solid; border-width: 1px;}
.b2 {background: #669;border-color: #99c #336 #336 #99c;color:#fff; border-style: solid; border-width: 1px; text-align: center}
.b3 {background: #fff;border-color: #ccf #669 #669 #ccf;}
.dmg { color: #FF0000; font-size: 18pt }
.clit { color: #0000FF; font-size: 18pt }
-->
</STYLE>
EOM
	print "<title>$main_title</title></head>\n";
	print "<body background=\"$backgif\" bgcolor=\"$bgcolor\" text=\"$text\" link=\"$link\" vlink=\"$vlink\" alink=\"$alink\">\n";
}
#-----------------#
#  TOP�y�[�W�\��  #
#-----------------#
sub html_top {
	&read_winner;

	&get_cookie;

	if($wkati) { $ritu = int(($wkati / $wtotal) * 100); }
	else { $ritu = 0; }

	open(IN,"<$recode_file");
	@recode = <IN>;
	close(IN);

	($rcount,$rname,$rsite,$rurl) = split(/<>/,$recode[0]);

	if($wsex) { $esex = "�j"; } else { $esex = "��"; }
	$next_ex = $wlv * $lv_up;

	if(!$wi_name){ $wi_name = "�Ȃ�"; }

	# �w�b�_�[�\��
	&header;

	# HTML�̕\��
	print <<"EOM";
<form action="$script" method="get">
<input type="hidden" name="mode" value="log_in">
<table border=0 width='100%'>
<tr>
<td><img src="$title_img"></td>
<td align="right" valign="top">
	<table border=1>
	<tr>
	<td align=center colspan=5 class=b2>�L�����N�^�[���쐬�ς݂̕��͂����炩��</td>
	</tr>
	<tr>
	<td class=b1>I D</td>
	<td><input type="text" size="10" name="id" value="$c_id"></td>
	<td class=b1>�p�X���[�h</td>
	<td><input type="password" size="10" name="pass" value="$c_pass"></td>
	<td><input type="submit" value="���O�C��"></td>
	</tr>
	</table>
</td>
</tr>
</table>
<hr size=0>
<small>
/ <a href="$homepage">$home_title</a> / <a href="$script?mode=item_shop">���퉮</a> / <a href="$script?mode=ranking">�p�Y�����̋L�^</a> / <a href="$syoku_html">�e�E�ƂɕK�v�ȓ����l</a> /
</form>
$kanri_message
<p>
���݂̘A���L�^�́A$rname����́u<A HREF=\"http\:\/\/$rurl\" TARGET=\"_blank\"><FONT SIZE=\"3\" COLOR=\"#6666BB\">$rsite</FONT></A>�v�A$rcount�A���ł��B�V�L�^���o�����T�C�g���̉��ɂ́A<IMG SRC="$mark">�}�[�N�����܂��B
<table border=0 width='100%'>
<tr>
<td width="500" valign="top">
	<table border=1 width="100%">
	<tr>
	<td colspan=5 align="center" class="b2"><font color="#FFFFFF">$wcount�A����</font></td>
	</tr>
	<tr>
	<td align="center" class="b1">�z�[���y�[�W</td>
	<td colspan="4"><a href="http\:\/\/$wurl"><b>$wsite</b></a>
EOM
	if($rurl eq "$wurl") {
		print "<IMG SRC=\"$mark\" border=0>\n";
	}
	print <<"EOM";
	</td>
	</tr>
	<tr>
	<td align="center" rowspan="8"><img src="$img_path/$chara_img[$wchara]"><p>�����F$ritu\%<br>����F$wi_name</td>
	<td align="center" class="b1">�Ȃ܂�</td><td><b>$wname</b></td>
	<td align="center" class="b1">����</td><td><b>$esex</b></td>
	</tr>
	<tr>
	<td align="center" class="b1">�E��</td><td><b>$chara_syoku[$wsyoku]</b></td>
	<td align="center" class="b1">�N���X</td><td><b>$wclass</b></td>
	</tr>
	<tr>
	<td align="center" class="b1">���x��</td><td><b>$wlv</b></td>
	<td align="center" class="b1">�o���l</td><td><b>$wex/$next_ex</b></td>
	</tr>
	<tr>
	<td align="center" class="b1">����</td><td><b>$wgold</b></td>
	<td align="center" class="b1">HP</td><td><b>$whp\/$wmaxhp</b></td>
	</tr>
	<tr>
	<td align="center" class="b1">��</td><td><b>$wn_0</b></td>
	<td align="center" class="b1">�m�\\</td><td><b>$wn_1</b></td>
	</tr>
	<tr>
	<td align="center" class="b1">�M�S</td><td><b>$wn_2</b></td>
	<td align="center" class="b1">������</td><td><b>$wn_3</b></td>
	</tr>
	<tr>
	<td align="center" class="b1">��p��</td><td><b>$wn_4</b></td>
	<td align="center" class="b1">����</td><td><b>$wn_5</b></td>
	</tr>
	<tr>
	<td align="center" class="b1">����</td><td><b>$wn_6</b></td>
	<td align="center" class="b1">�J���}</td><td><b>$wlp</b></td>
	</tr>
	<tr>
	<td colspan=5 align="center">$lname �� <A HREF=\"http\:\/\/$lurl\" TARGET=\"_blank\">$lsite</A> �ɏ����I�I</td>
	</tr>
	</table>
</td>
<td valign="top" class=small>
[<B><FONT COLOR="#FF9933">$main_title �̗V�ѕ�</FONT></B>]
<OL>
<LI>�܂��A�u�V�K�L�����N�^�[�o�^�v�{�^���������āA�L�����N�^�[���쐬���܂��B
<LI>�L�����N�^�[�̍쐬������������A���̃y�[�W�̉E��ɂ���Ƃ��납�烍�O�C�����āA���Ȃ���p�̃X�e�[�^�X��ʂɓ���܂��B
<LI>�����ł��Ȃ��̍s����I�����邱�Ƃ��ł��܂��B
<LI>��x�L�����N�^�[���쐬������A�E��̂Ƃ��납�烍�O�C�����ėV�т܂��B�V�K�ɃL�����N�^�[������̂́A��l�Ɉ�̃L�����N�^�[�݂̂ł��B
<LI>����́AHP�o�g���[�ł͂Ȃ��A�L�����o�g���[�ł��B�L�����N�^�[����ĂĂ����Q�[���ł��B
<LI>�\\�͂�U�蕪���邱�Ƃ��ł��L�����N�^�[�̔\\�͂��������Ō��߂邱�Ƃ��ł��܂��B(�����Ō��߂��\\�͂͂����܂�ɂ����㏸���Ȃ��̂ŁA�T�d��)
<LI><b>$limit��</b>�ȏ㓬��Ȃ���΁A�L�����N�^�[�̃f�[�^���폜����܂��B
<LI>��x�퓬�����<b>$b_time</b>�b�o�߂��Ȃ��ƍĂѐ퓬�ł��܂���B
</OL>
[<B><FONT COLOR="#FF9933">�V�K�L�����N�^�쐬</FONT></B>]<BR>
���̃{�^���������āA���Ȃ��̃L�����N�^�[���쐬���܂��B
<FORM ACTION="$script" METHOD="POST">
<INPUT TYPE="hidden" NAME="mode" VALUE="chara_make">
<INPUT TYPE="submit" VALUE="�V�K�L�����N�^�[�쐬">
</FORM>
</td>
</tr>
</table>
</small>
EOM

	# �t�b�^�[�\��
	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub item_buy {
	if($in{'id'} eq "") {
		&error("ID�����͂���Ă��܂���B");
	}elsif($in{'pass'} eq ""){
		&error("�p�X���[�h�����͂���Ă��܂���B");
	}elsif($in{'item_no'} eq ""){
		&error("�A�C�e����I��ł��������B");
	}
	$item_id = $in{'id'};
	$item_pass = $in{'pass'};

	open(IN,"<$item_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	&get_host;

	$date = time();

	# �t�@�C�����b�N
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(IN,"<$chara_file");
	@item_chara = <IN>;
	close(IN);

	$hit=0;@item_new=();
	foreach(@item_chara){
		($iid,$ipass,$isite,$iurl,$iname,$isex,$ichara,$in_0,$in_1,$in_2,$in_3,$in_4,$in_5,$in_6,$isyoku,$iclass,$ihp,$imaxhp,$iex,$ilv,$igold,$ilp,$itotal,$ikati,$iwaza,$ii_name,$ii_dmg,$imons,$ihost,$idate) = split(/<>/);
		if($iid eq "$item_id") {
			if ($ipass ne $item_pass) { &error('�p�X���[�h���Ⴂ�܂��B'); }
			if($igold < $i_gold) { &error("����������܂���"); }
			else { $igold = $igold - $i_gold; }
			unshift(@item_new,"$iid<>$ipass<>$isite<>$iurl<>$iname<>$isex<>$ichara<>$in_0<>$in_1<>$in_2<>$in_3<>$in_4<>$in_5<>$in_6<>$isyoku<>$iclass<>$imaxhp<>$imaxhp<>$iex<>$ilv<>$igold<>$ilp<>$itotal<>$ikati<>$iwaza<>$i_name<>$i_dmg<>$imons<>$host<>$idate<>\n");
			$hit=1;
		}else{
			push(@item_new,"$_");
		}
	}

	if(!$hit) { &error("�L�����N�^�[��������܂���"); }

	open(OUT,">$chara_file");
	print OUT @item_new;
	close(OUT);

	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	&header;

	print <<"EOM";
<h1>�A�C�e���𔃂��܂���</h1>
<hr size=0>
<p>
<form action="$script" method="get">
<input type=hidden name=id value="$item_id">
<input type=hidden name=pass value="$item_pass">
<input type=hidden name=mode value=log_in>
<input type=submit value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}
#----------------#
#  �A�C�e���\��  #
#----------------#
sub item_shop {
	open(IN,"<$item_file");
	@item_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>�A�C�e���V���b�v</h1>
<hr size=0>
<p>
<form action="$script" method="post">
���������A�C�e�����`�F�b�N���A���Ȃ���ID�ƃp�X���[�h����͂��Ă��������B
<table border=1>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>�З�</th><th>���i</th>
EOM

	foreach(@item_array){
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr>\n";
		print "<td><input type=radio name=item_no value=\"$ino\"></td><td align=right>$ino</td><td>$iname</td><td align=center>$idmg</td><td align=center>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</tr>
</table>
<p>
���Ȃ��̃L�����N�^�[��ID�ƃp�X���[�h����͂��ă{�^���������Ă��������B<br>
ID�F<input type=text name=id size=10>
PASS�F<input type=text name=pass size=10>
<input type=hidden name=mode value=item_buy>
<input type=submit value="�A�C�e���𔃂�">
</form>
EOM

	&footer;

	exit;
}
#-------------------------------#
#  ���b�N�t�@�C���Fsymlink�֐�  #
#-------------------------------#
sub lock1 {
	local($retry) = 5;
	while (!symlink(".", $lockfile)) {
		if (--$retry <= 0) { &error("LOCK is BUSY"); }
		sleep(1);
	}
}
#----------------------------#
#  ���b�N�t�@�C���Fopen�֐�  #
#----------------------------#
sub lock2 {
	local($retry) = 0;
	foreach (1 .. 5) {
		if (-e $lockfile) { sleep(1); }
		else {
			open(LOCK,">$lockfile") || &error("Can't Lock");
			close(LOCK);
			$retry = 1;
			last;
		}
	}
	if (!$retry) { &error("���΂炭���҂��ɂȂ��Ă�������(^^;)"); }
}
#----------------#
#  ���O�C�����  #
#----------------#
sub log_in {
	$chara_flag=1;

	# �t�@�C�����b�N
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(IN,"<$chara_file");
	@log_in = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_in){
		($kid,$kpass,$ksite,$kurl,$kname,$ksex,$kchara,$kn_0,$kn_1,$kn_2,$kn_3,$kn_4,$kn_5,$kn_6,$ksyoku,$kclass,$khp,$kmaxhp,$kex,$klv,$kgold,$klp,$ktotal,$kkati,$kwaza,$ki_name,$ki_dmg,$kmons,$khost,$kdate) = split(/<>/);
		if($in{'id'} eq "$kid" and $in{'pass'} eq "$kpass") {
			$hit=1; last;
		}
	}

	$ltime = time();
	$ltime = $ltime - $kdate;
	$vtime = $b_time - $ltime;
	$mtime = $m_time - $ltime;
	if($in{'id'} ne "$kid") {&error("�I�[�v���G���[�AID�E�p�X���[�h������������܂���B");}
	
	if(!$hit) { &error("���͂��ꂽID�͓o�^����Ă��܂���B���̓p�X���[�h���Ⴂ�܂��B"); }

	if($ksex) { $esex = "�j"; } else { $esex = "��"; }
	$next_ex = $klv * $lv_up;

	&header;

	print <<"EOM";
<h1>$kname����p�X�e�[�^�X���</h1>
<hr size=0>
EOM
	if($ltime < $b_time and $ktotal){
	print <<"EOM";
<FORM NAME="form1">
�`�����v�Ɠ�����܂Ŏc��<INPUT TYPE="text" NAME="clock" SIZE="3" VALUE="$vtime">�b�ł��B0�ɂȂ�ƁA�����I�ɍX�V���܂��̂Ńu���E�U�̍X�V�͉����Ȃ��ŉ������B
</FORM>
EOM
	}
	print <<"EOM";
<form action="$script" method="post">
<table border=0>
<tr>
<td valign=top width='50%'>
<table border=1>
<tr>
<td colspan="5" class="b2" align="center">�z�[���y�[�W�f�[�^</td>
</tr>
<tr>
<td class="b1">�z�[���y�[�W��</td>
<td colspan="4"><input type="text" name=site value="$ksite" size=50></td>
</tr>
<tr>
<td class="b1">�z�[���y�[�W��URL</td>
<td colspan="4"><input type="text" name=url value="http\:\/\/$kurl" size=60></td>
</tr>
<tr>
<td colspan="5" class="b2" align="center">�L�����N�^�[�f�[�^</td>
</tr>
<tr>
<td rowspan="8" align="center"><img src="$img_path/$chara_img[$kchara]"><br>����F$ki_name</td>
<td class="b1">�Ȃ܂�</td>
<td><input type="text" name=c_name value="$kname" size=10></td>
<td class="b1">����</td>
<td>$esex</td>
</tr>
<tr>
<td class="b1">�E��</td>
<td>$chara_syoku[$ksyoku]</td>
<td class="b1">�N���X</td>
<td>$kclass</td>
</tr>
<tr>
<td class="b1">���x��</td>
<td>$klv</td>
<td class="b1">�o���l</td>
<td>$kex/$next_ex</td>
</tr>
<tr>
<td class="b1">����</td>
<td>$kgold</td>
<td class="b1">HP</td>
<td>$khp\/$kmaxhp</td>
</tr>
<tr>
<td class="b1">��</td>
<td>$kn_0</td>
<td class="b1">�m�\\</td>
<td>$kn_1</td>
</tr>
<tr>
<td class="b1">�M�S</td>
<td>$kn_2</td>
<td class="b1">������</td>
<td>$kn_3</td>
</tr>
<tr>
<td class="b1">��p��</td>
<td>$kn_4</td>
<td class="b1">����</td>
<td>$kn_5</td>
</tr>
<tr>
<td class="b1">����</td>
<td>$kn_6</td>
<td class="b1">�J���}</td>
<td>$klp</td>
</tr>
<tr>
<td class="b1">�Z�������R�����g<br>
<small>�i���p$waza_maxs�����ȓ��j</small></td>
<td colspan="4"><input type="text" name=waza value="$kwaza" size=50></td>
</tr>
<tr>
<td colspan="5" align="center">
<input type="hidden" name=mode value=battle>
<input type="hidden" name=id value="$kid">
<input type="hidden" name=pass value="$kpass">
EOM
	if($ltime >= $b_time or !$ktotal) {
		print "<input type=\"submit\" value=\"�`�����v�ɒ���\">\n";
	}else{
		print "$vtime�b�㓬����悤�ɂȂ�܂��B\n";
	}

	print <<"EOM";
</td>
</tr>
</table>
</form>
</td>
<td valign="top">
<form action="$script" method="post">
�y���ݓ]�E�ł���E�ƈꗗ�z<br>
<select name=syoku>
<option value="no">�I�����Ă��������B
EOM

	open(IN,"<$syoku_file");
	@syoku = <IN>;
	close(IN);

	$i=0;$hit=0;
	foreach(@syoku){
		($a,$b,$c,$d,$e,$f,$g) = split(/<>/);
		if($kn_0 >= $a and $kn_1 >= $b and $kn_2 >= $c and $kn_3 >= $d and $kn_4 >= $e and $kn_5 >= $f and $kn_6 >= $g and $ksyoku != $i) {
			print "<option value=\"$i\">$chara_syoku[$i]\n";
			$hit=1;
		}
		$i++;
	}
	print <<"EOM";
</select>
<input type=hidden name=id value="$kid">
<input type=hidden name=pass value="$kpass">
<input type=hidden name=mode value="tensyoku">
EOM

	if(!$hit) { print "���ݓ]�E�ł���E�Ƃ͂���܂���"; }
	else { print "<input type=submit value=\"�]�E����\">\n"; }

	print <<"EOM";
<br>
�@<small>�� �]�E����ƁA�S�Ă̔\\�͒l���]�E�����E�Ƃ̏����l�ɂȂ�܂��B�܂��ALV��1�ɂȂ�܂��B</small>
</form>
<form action="$script" method="post">
�y�����Ɛ킢�C�s�ł��܂��z<br>
<input type=hidden name=id value="$kid">
<input type=hidden name=pass value="$kpass">
<input type=hidden name=mode value="monster">
EOM

	if($ltime >= $m_time or !$ktotal) {
		print "<input type=submit value=\"�����X�^�[�Ɠ���\"><br>\n";
	}else{
		print "$mtime�b�㓬����悤�ɂȂ�܂��B<br>\n";
	}

	$yado_gold = $yado_dai * $klv;

	print <<"EOM";
�@<small>���C�s�̗��ɂ����܂��B</small>
</form>
<form action="$script" method="post">
�y���̏h�z<br>
<input type=hidden name=id value="$kid">
<input type=hidden name=pass value="$kpass">
<input type=hidden name=mode value="yado">
<input type=submit value="�̗͂���"><br>
�@<small>���̗͂��񕜂��邱�Ƃ��ł��܂��B<b>$yado_gold</b>G�K�v�ł��B���݃`�����v�̕����񕜂ł��܂��B���܂߂ɉ񕜂���ΘA���L�^���E�E�E�B</small>
</form>
<form action="$script" method="post">
�y���̃L�����N�^�[�փ��b�Z�[�W�𑗂�z<br>
<input type="text" name=mes size=50><br>
<select name=mesid>
<option value="">���鑊���I��
EOM

	open(IN,"<$chara_file");
	@MESSAGE = <IN>;
	close(IN);

	foreach(@MESSAGE) {
		($did,$dpass,$dsite,$durl,$dname) = split(/<>/);
		if($kid eq $did) { next; }
		print "<option value=$did>$dname�����\n";
	}

	print <<"EOM";
</select>
<input type=hidden name=id value="$kid">
<input type=hidden name=name value="$kname">
<input type=hidden name=pass value="$kpass">
<input type=hidden name=mode value="message">
<input type=submit value="���b�Z�[�W�𑗂�"><br>
�@<small>�����̃L�����N�^�[�փ��b�Z�[�W�𑗂邱�Ƃ��ł��܂��B�i���p$mes_maxs�����ȓ��j</small>
</form>
</td>
</tr>
</table>
�y�͂��Ă��郁�b�Z�[�W�z�\\����<b>$max_gyo</b>���܂�<br>
EOM

	open(IN,"<$message_file");
	@MESSAGE_LOG = <IN>;
	close(IN);

	$hit=0;$i=1;
	foreach(@MESSAGE_LOG){
		($pid,$hid,$hname,$hmessage,$hhname,$htime) = split(/<>/);
		if($kid eq "$pid"){
			if($max_gyo < $i) { last; }
			print "<hr size=0><small><b>$hname����</b>�@�� �u<b>$hmessage</b>�v($htime)</small><br>\n";
			$hit=1;$i++;
		}elsif($kid eq "$hid"){
			print "<hr size=0><small>$kname���񂩂�$hhname����ց@�� �u$hmessage�v($htime)</small><br>\n";
		}
	}
	if(!$hit){ print "<hr size=0>$kname���񈶂Ẵ��b�Z�[�W�͂���܂���<p>\n"; }
	print "<hr size=0><p>";

	&footer;

	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	$chara_flag=0;

	exit;
}
#----------------#
#  �o�^�������  #
#----------------#
sub make_end {
	if($chara_stop){ &error("���݃L�����N�^�[�̍쐬�o�^�͂ł��܂���"); }
	if ($in{'id'} =~ m/[^0-9a-zA-Z]/)
	{&error("ID�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); }
	if ($in{'pass'} =~ m/[^0-9a-zA-Z]/)
	{&error("�p�X���[�h�ɔ��p�p�����ȊO�̕������܂܂�Ă��܂��B"); }
	# �E�Ɩ��I���̏ꍇ
		if($in{'syoku'} eq "") {
		if($in{'id'} eq "" or length($in{'id'}) < 4 or length($in{'id'}) > 8) { &error("ID�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B"); }
		elsif($in{'pass'} eq "" or length($in{'pass'}) < 4 or length($in{'pass'}) > 8) { &error("�p�X���[�h�́A4�����ȏ�A8�����ȉ��œ��͂��ĉ������B"); }
		elsif($in{'site'} eq "") { &error("�z�[���y�[�W�������L���ł�"); }
		elsif($in{'url'} eq "") { &error("URL�����L���ł�"); }
		elsif($in{'c_name'} eq "") { &error("�L�����N�^�[�̖��O�����L���ł�"); }
		elsif($in{'sex'} eq "") { &error("���ʂ��I������Ă��܂���"); }

		$g = $in{'n_0'} + $in{'n_1'} + $in{'n_2'} + $in{'n_3'} + $in{'n_4'} + $in{'n_5'} + $in{'n_6'};

		if($g > 10) { &error("�|�C���g�̐U�蕪�����������܂��B�U�蕪���̍��v���A10�ȉ��ɂ��Ă��������B"); }

		&header;

		print "<h1>�E�ƑI�����</h1><hr size=0>\n";
		print "���Ȃ����Ȃ邱�Ƃ��ł���E�Ƃ͈ȉ��̂Ƃ���ł��B<p>\n";
		print "<form action=\"$script\" method=\"post\">\n";
		print "<input type=hidden name=mode value=regist>\n";
		print "<select name=syoku>\n";

		open(IN,"<$syoku_file");
		@syokudata = <IN>;
		close(IN);

		@kn = map { $in{'n_'.$_} + $kiso_nouryoku[$_] } 0..$#kiso_nouryoku;

		$i=0;$hit=0;
		foreach(@syokudata){
			@buffer = split(/<>/);
			if($kn[0] >= $buffer[0] && $kn[1] >= $buffer[1] && $kn[2] >= $buffer[2] && $kn[3] >= $buffer[3] && $kn[4] >= $buffer[4] && $kn[5] >= $buffer[5] && $kn[6] >= $buffer[6]){
				print "<option value=\"$i\">$chara_syoku[$i]\n";
				$hit=1;
				}
			$i++;
		}
		if(!$hit){print "<option value=\"0\">$chara_syoku[0]\n";}

		print "</select>\n";
		print "<input type=hidden name=new value=new>\n";
		print "<input type=hidden name=id value=\"$in{'id'}\">\n";
		print "<input type=hidden name=pass value=\"$in{'pass'}\">\n";
		print "<input type=hidden name=site value=\"$in{'site'}\">\n";
		print "<input type=hidden name=url value=\"$in{'url'}\">\n";
		print "<input type=hidden name=c_name value=\"$in{'c_name'}\">\n";
		print "<input type=hidden name=sex value=\"$in{'sex'}\">\n";
		print "<input type=hidden name=chara value=\"$in{'chara'}\">\n";
		print "<input type=hidden name=n_0 value=\"$in{'n_0'}\">\n";
		print "<input type=hidden name=n_1 value=\"$in{'n_1'}\">\n";
		print "<input type=hidden name=n_2 value=\"$in{'n_2'}\">\n";
		print "<input type=hidden name=n_3 value=\"$in{'n_3'}\">\n";
		print "<input type=hidden name=n_4 value=\"$in{'n_4'}\">\n";
		print "<input type=hidden name=n_5 value=\"$in{'n_5'}\">\n";
		print "<input type=hidden name=n_6 value=\"$in{'n_6'}\">\n";
		print "<input type=submit value=\"���̐E�Ƃ�OK\"></form>\n";

		&footer;

		exit;
	}else{
		if($in{'sex'}) { $esex = "�j"; } else { $esex = "��"; }
		$next_ex = $lv * $lv_up;

		&header;

		print <<"EOM";
<h1>�o�^�������</h1>
�ȉ��̓��e�œo�^���������܂����B
<hr size=0>
<p>
<table border=1>
<tr>
<td class="b1">�z�[���y�[�W</td>
<td colspan="4"><a href="http\:\/\/$in{'url'}">$in{'site'}</a></td>
</tr>
<tr>
<td rowspan="8" align="center"><img src="$img_path/$chara_img[$in{'chara'}]"></td>
<td class="b1">�Ȃ܂�</td>
<td>$in{'c_name'}</td>
<td class="b1">����</td>
<td>$esex</td>
</tr>
<tr>
<td class="b1">�E��</td>
<td>$chara_syoku[$in{'syoku'}]</td>
<td class="b1">����</td>
<td>$gold</td>
</tr>
<tr>
<td class="b1">���x��</td>
<td>$lv</td>
<td class="b1">�o���l</td>
<td>$ex/$next_ex</td>
</tr>
<tr>
<td class="b1">HP</td>
<td>$hp</td>
<td class="b1"></td>
<td></td>
</tr>
<tr>
<td class="b1">��</td>
<td>$n_0</td>
<td class="b1">�m�\\</td>
<td>$n_1</td>
</tr>
<tr>
<td class="b1">�M�S</td>
<td>$n_2</td>
<td class="b1">������</td>
<td>$n_3</td>
</tr>
<tr>
<td class="b1">��p��</td>
<td>$n_4</td>
<td class="b1">����</td>
<td>$n_5</td>
</tr>
<tr>
<td class="b1">����</td>
<td>$n_6</td>
<td class="b1">�J���}</td>
<td>$lp</td>
</tr>
</table>
<form action="$script" method="post">
<input type="hidden" name=mode value=log_in>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="�X�e�[�^�X��ʂ�">
</form>
EOM

		&footer;

		exit;
	}
}
#--------------#
#  ���b�Z�[�W  #
#--------------#
sub message {
	if($in{'mes'} eq "") { &error("���b�Z�[�W���L������Ă��܂���"); }
	if($in{'mesid'} eq "") { &error("���肪�w�肳��Ă��܂���"); }

	&get_time;

	# �t�@�C�����b�N
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(IN,"<$message_file");
	@mes_regist = <IN>;
	close(IN);

	open(IN,"<$chara_file");
	@MESSAGE = <IN>;
	close(IN);

	$hit = $for = 0;
	foreach(@MESSAGE) {
		($did,$dpass,$dsite,$durl,$dname) = split(/<>/);
		if($in{'mesid'} eq "$did") { $for = $_; }
		if(($in{'id'} eq $did) and ($in{'pass'} eq $dpass)) { $hit = 1; }
		if ($hit and $for) { last; }
	}
	if (!$hit or !$for) { &error('���悪�s���ł��B�܂���ID�A�p�X���[�h���Ⴂ�܂��B'); }
	($did,$dpass,$dsite,$durl,$dname) = split(/<>/, $for);


	$mes_max = @mes_regist;

	if($mes_max > $max) { pop(@mes_regist); }

	unshift(@mes_regist,"$in{'mesid'}<>$in{'id'}<>$in{'name'}<>$in{'mes'}<>$dname<>$gettime<>\n");

	open(OUT,">$message_file");
	print OUT @mes_regist;
	close(OUT);

	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	&header;

	print <<"EOM";
<h1>$dname����փ��b�Z�[�W�𑗂�܂����B</h1>
<hr size=0>
<form action="$script" method="get">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value="$in{'id'}">
<input type=hidden name=pass value="$in{'pass'}">
<input type=submit value="���O�C����ʂ֖߂�">
</form>
EOM

	&footer;

	exit;
}
#----------------------#
#  �����X�^�[�Ƃ̐퓬  #
#----------------------#
sub monster {

	open(IN,"<$chara_file");
	@battle = <IN>;
	close(IN);

	foreach(@battle){
		($kid,$kpass,$ksite,$kurl,$kname,$ksex,$kchara,$kn_0,$kn_1,$kn_2,$kn_3,$kn_4,$kn_5,$kn_6,$ksyoku,$kclass,$khp,$kmaxhp,$kex,$klv,$kgold,$klp,$ktotal,$kkati,$kwaza,$ki_name,$ki_dmg,$kmons,$khost,$kdate) = split(/<>/);
		if($in{'id'} eq "$kid") { last; }
	}
	if (($in{'id'} ne $kid) or ($in{'pass'} ne $kpass)) {&error('ID�A�p�X���[�h���Ⴂ�܂�');}

	$ltime = time();
	$ltime = $ltime - $kdate;
	$vtime = $b_time - $ltime;
	$mtime = $m_time - $ltime;
	if($in{'id'} ne "$kid") {&error("�I�[�v���G���[�AID�E�p�X���[�h������������܂���B");}
	
	if($ltime < $m_time and $ktotal) {
		&error("$mtime�b�㓬����悤�ɂȂ�܂��B<br>\n");
	}

	if(!$kmons) { &error("��x�L�����N�^�[�Ɠ����Ă�������"); }

	open(IN,"<$monster_file");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$r_no = int(rand($r_no));

	($mname,$mex,$mhp,$msp,$mdmg) = split(/<>/,$MONSTER[$r_no]);

	if($in{'site'}) { $ksite = $in{'site'}; }
	if($in{'url'}) { $kurl = $in{'url'}; }
	if($in{'waza'}) { $kwaza = $in{'waza'}; }
	if($in{'c_name'}) { $kname = $in{'c_name'}; }
	$khp_flg = $khp;
	$mhp = int(rand($mhp)) + $msp;
	$mhp_flg = $mhp;

	$i=1;$j=0;@battle_date=();
	foreach(1..$turn) {
		$dmg1 = $klv * (int(rand(5)) + 1);
		$dmg2 = (int(rand($mdmg)) + 1) + $mdmg;
		$clit1 = "";
		$clit2 = "";
		$com1 = "";
		$com2 = "$mname���P�����������I�I";
		$kawasi1 = "";
		$kawasi2 = "";

			# ����҃_���[�W�v�Z
			if($ksyoku == 0){
				$dmg1 = $dmg1 + int(rand($kn_0));
				$com1 = "$kname�́A���Ő؂�����I�I<p>";
			}elsif($ksyoku == 1){
				$dmg1 = $dmg1 * int(rand($kn_1));
				$com1 = "$kname�́A���@���������I�I<p>";
			}elsif($ksyoku == 2){
				$dmg1 = $dmg1 * int(rand($kn_2));
				$com1 = "$kname�́A���@���������I�I<p>";
			}elsif($ksyoku == 3){
				$dmg1 = $dmg1 + int(rand($kn_4));
				$com1 = "$kname�́A�w�ォ��؂�����I�I<p>";
			}elsif($ksyoku == 4){
				$dmg1 = $dmg1 + int(rand($kn_3)) + int(rand($kn_0));
				$com1 = "$kname�́A�|�ōU���I�I<p>";
			}elsif($ksyoku == 5){
				$dmg1 = $dmg1 * (int(rand($kn_1)) + int(rand($kn_4)));
				$com1 = "$kname�́A���@���������I�I<p>";
			}elsif($ksyoku == 6){
				$dmg1 = $dmg1 * (int(rand($kn_1)) + int(rand($kn_4)));
				$com1 = "$kname�́A��̂��̂����I�I<p>";
			}elsif($ksyoku == 7){
				$dmg1 = $dmg1 * (int(rand($kn_1)) + int(rand($kn_3)));
				$com1 = "$kname�́A���\\�͂��g�����I�I<p>";
			}elsif($ksyoku == 8){
				$dmg1 = $dmg1 * (int(rand($kn_1)) + int(rand($kn_2)));
				$com1 = "$kname�́A���얂�@�ƁA�_�����@�𓯎��ɏ������I�I<p>";
			}elsif($ksyoku == 9){
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2));
				$com1 = "$kname�́A����˂��h�����I�I<p>";
			}elsif($ksyoku == 10){
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2));
				$com1 = "$kname�́A�_�����@�������A���Ő؂�����I�I<p>";
			}elsif($ksyoku == 11){
				$dmg1 = $dmg1 + int(rand($kn_4)) + int(rand($kn_5));
				$com1 = "$kname�́A�����Ȃ������Ő؂�����I�I<p>";
			}elsif($ksyoku == 12){
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2));
				$com1 = "$kname�́A��������I�I<p>";
			}elsif($ksyoku == 13){
				$dmg1 = $dmg1 + int(rand($kn_0)) + int(rand($kn_2));
				$com1 = "$kname�́A�R������I�I<p>";
			}

			if(int(rand(20)) == 0) {
				$clit1 = "<font size=5>$kname�u<b>$kwaza</b>�v</font><p><b class=\"clit\">�N���e�B�J���I�I</b>";
				$dmg1 = $dmg1 * 2;
			}

			if(int(rand(30)) == 0) {
				$clit2 = "<b class=\"clit\">�N���e�B�J���I�I</b>";
				$dmg2 = int($dmg2 * 1.5);
			}

		$battle_date[$j] = <<"EOM";
<TABLE BORDER=0>
<TR>
	<TD CLASS="b2" COLSPAN="3" ALIGN="center">
	$i�^�[��
	</TD>
</TR>
<TR>
<TD>
<TABLE BORDER=1>
<TR>
	<TD CLASS="b1">
	�Ȃ܂�
	</TD>
	<TD CLASS="b1">
	HP
	</TD>
	<TD CLASS="b1">
	�E��
	</TD>
	<TD CLASS="b1">
	LV
	</TD>
</TR>
<TR>
	<TD>
	$kname
	</TD>
	<TD>
	$khp_flg\/$kmaxhp
	</TD>
	<TD>
	$chara_syoku[$ksyoku]
	</TD>
	<TD>
	$klv
	</TD>
</TR>
</TABLE>
</TD>
<TD>
<FONT SIZE=5 COLOR="#9999DD">VS</FONT>
</TD>
<TD>
<TABLE BORDER=1>
<TR>
	<TD CLASS="b1">
	�Ȃ܂�
	</TD>
	<TD CLASS="b1">
	HP
	</TD>
</TR>
<TR>
	<TD>
	$mname
	</TD>
	<TD>
	$mhp/$mhp_flg
	</TD>
</TR>
</TABLE>
</TD>
</TR>
</TABLE>
<p>
$com1 $clit1 $kawasi2 $mname �� <font class="dmg"><b>$dmg1</b></font> �̃_���[�W��^�����B<p>
$com2 $clit2 $kawasi1 $kname �� <font class="dmg"><b>$dmg2</b></font> �̃_���[�W��^�����B<p>
EOM

		$khp_flg = $khp_flg - $dmg2;
		$mhp = $mhp - $dmg1;

		if($mhp <= 0) { $win = 1; last; }
		elsif($khp_flg <= 0) { $win = 0; last; }

		$i++;
		$j++;
	}

	if($win) {
		$ktotal += 1;
		$kkati += 1;
		$kex = $kex + $mex;
		$kmons -= 1;
		$gold = $klv * 10 + int(rand($klp));
		$kgold = $kgold + $gold;
		$comment = "<b><font size=5>$kname�́A�퓬�ɏ��������I�I</font></b><p>";
	}else{
		$ktotal += 1;
		$mex = int(rand($klp));
		$kex = $kex + $mex;
		$kmons -= 1;
		if($kgold) { $kgold = int($kgold / 2); }
		else { $kgold = 0; }
		$comment = "<b><font size=5>$kname�́A�퓬�ɕ������E�E�E�B</font></b><p>";
	}

	if($kex >= ($klv * $lv_up)) { &lv_up; }

	$khp = $khp_flg + int(rand($kn_3));
	if($khp > $kmaxhp) { $khp = $kmaxhp; }
	if($khp <= 0) { $khp = $kmaxhp; }

	&regist;

	&header;

	print "<h1>$kname�́A$mname�ɐ킢�𒧂񂾁I�I</h1><hr size=0><p>\n";

	$i=0;
	foreach(@battle_date){
		print "$battle_date[$i]";
		$i++;
	}
	
	if($win) { print "$comment<p>$kname�́A$mex�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<p>\n"; }
	else { print "$comment<p>$kname�́A$mex�̌o���l����ɓ��ꂽ�B�����������ɂȂ����B<p>\n"; }

	&footer;

	exit;
}
#------------------#
#  �����L���O���  #
#------------------#
sub ranking {
	open(IN,"<$chara_file");
	@RANKING = <IN>;
	close(IN);

	$sousu = @RANKING;

	@tmp1 = @tmp2 = ();
	foreach (@RANKING) {
 		my ($aa,$bb,$cc,$dd,$ee,$ff,$gg,$hh,$ii,$jj,$kk,$ll,$mm,$nn,$oo,$oo2,$pp,$qq,$second,$first) = split /<>/;
 		push(@tmp1, $first);
 		push(@tmp2, $second);
	}
	@RANKING = @RANKING[sort {$tmp1[$b] <=> $tmp1[$a] or
			$tmp2[$b] <=> $tmp2[$a]} 0 .. $#tmp1];

	$ima = time();

	&header;

	print <<"EOM";
<h1>�p�Y�����̋L�^</h1><hr size=0>
���ݓo�^����Ă���L�����N�^�[<b>$sousu</b>�l�����x��TOP<b>$rank_top</b>��\\�����Ă��܂��B
<p>
<table border=1>
<tr>
<th></th><th>�Ȃ܂�</th><th>�E��</th><th>�z�[���y�[�W</th><th>���x��</th><th>�o���l</th><th>HP</th><th>��</th><th>�폜�܂�</th>
</tr>
EOM

	$i=1;
	foreach(@RANKING){
		($rid,$rpass,$rsite,$rurl,$rname,$rsex,$rchara,$rn_0,$rn_1,$rn_2,$rn_3,$rn_4,$rn_5,$rn_6,$rsyoku,$rclass,$rhp,$rmaxhp,$rex,$rlv,$rgold,$rlp,$rtotal,$rkati,$rwaza,$ri_name,$ri_dmg,$rmons,$rhost,$rdate) = split(/<>/);
		if($i > $rank_top) { last; }
		$rdate = $rdate + (86400*$limit);
		$niti = $rdate - $ima;
		$niti = int($niti / 86400);
		print "<tr>\n";
		print "<td align=center>$i</td><td>$rname</td><td>$chara_syoku[$rsyoku]</td><td><a href=\"http\:\/\/$rurl\">$rsite</a></td><td align=center>$rlv</td><td align=center>$rex</td><td align=center>$rhp\/$rmaxhp</td><td align=center>$rn_0</td><td align=center>����$niti��</td>\n";
		print "</tr>\n";
		$i++;
	}

	print "</table><p>\n";

	&footer;

	exit;
}
#--------------------#
#  �`�����v�ǂݍ���  #
#--------------------#
sub read_winner {
	open(IN,"<$winner_file");
	@winner = <IN>;
	close(IN);

	($wid,$wpass,$wsite,$wurl,$wname,$wsex,$wchara,$wn_0,$wn_1,$wn_2,$wn_3,$wn_4,$wn_5,$wn_6,$wsyoku,$wclass,$whp,$wmaxhp,$wex,$wlv,$wgold,$wlp,$wtotal,$wkati,$wwaza,$wi_name,$wi_dmg,$wmons,$whost,$wdate,$wcount,$lsite,$lurl,$lname) = split(/<>/,$winner[0]);
}

#----------------#
#  �������ݏ���  #
#----------------#
sub regist {
	&set_cookie;

	&get_host;

	$date = time();

	# �t�@�C�����b�N
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(IN,"<$chara_file");
	@regist = <IN>;
	close(IN);

	$hit=0;@new=();
	foreach(@regist){
		($cid,$cpass,$csite,$curl,$cname,$csex,$cchara,$cn_0,$cn_1,$cn_2,$cn_3,$cn_4,$cn_5,$cn_6,$csyoku,$cclass,$chp,$cmaxhp,$cex,$clv,$cgold,$clp,$ctotal,$ckati,$cwaza,$ci_name,$ci_dmg,$cmons,$chost,$cdate) = split(/<>/);
		if($cid eq "$in{'id'}" and $in{'new'} eq 'new') {
			&error("����ID�͂��łɓo�^����Ă��܂�");
		}elsif($curl eq "$in{'url'}" and $in{'new'} eq 'new'){
			&error("����URL�͂��łɓo�^����Ă��܂�");
		}elsif($host eq "$chost" and $in{'new'} eq 'new'){
			&error("�P�l�P�L�����N�^�[�ł��B");
		}elsif($cid eq "$kid"){
			unshift(@new,"$kid<>$kpass<>$ksite<>$kurl<>$kname<>$ksex<>$kchara<>$kn_0<>$kn_1<>$kn_2<>$kn_3<>$kn_4<>$kn_5<>$kn_6<>$ksyoku<>$kclass<>$khp<>$kmaxhp<>$kex<>$klv<>$kgold<>$klp<>$ktotal<>$kkati<>$kwaza<>$ki_name<>$ki_dmg<>$kmons<>$host<>$date<>\n");
			$hit=1;
		}else{
			if(($date - $cdate) > (86400 * $limit)) { &del_message($cid);next; }
			push(@new,"$_");
		}
	}

	if(!$hit and $in{'new'} eq 'new'){
		$g = $in{'n_0'} + $in{'n_1'} + $in{'n_2'} + $in{'n_3'} + $in{'n_4'} + $in{'n_5'} + $in{'n_6'};
		if($g > 10) { &error("�|�C���g�̐U�蕪�����������܂��B�U�蕪���̍��v���A10�ȉ��ɂ��Ă��������B"); }

		open(IN,"<$syoku_file");
		@syokudata = <IN>;
		close(IN);

		($a,$b,$c,$d,$e,$f,$g) = split(/<>/,$syokudata[$in{'syoku'}]);

		if(!$a) { $a = $kiso_nouryoku[0]; }
		if(!$b) { $b = $kiso_nouryoku[1]; }
		if(!$c) { $c = $kiso_nouryoku[2]; }
		if(!$d) { $d = $kiso_nouryoku[3]; }
		if(!$e) { $e = $kiso_nouryoku[4]; }
		if(!$f) { $f = $kiso_nouryoku[5]; }
		if(!$g) { $g = $kiso_nouryoku[6]; }

		@kn = map { $in{'n_'.$_} + $kiso_nouryoku[$_] } 0..$#kiso_nouryoku;

		if($kn[0]<$a||$kn[1]<$b||$kn[2]<$c||$kn[3]<$d||$kn[4]<$e||$kn[5]<$f||$kn[6]<$h){
			if($in{'syoku'}){
				&error('���̐E�ƂɂȂ邽�߂̃X�e�[�^�X���s�����Ă��܂�');
			}
		}

		$lp=int(rand(15));
		$hp = int(($in{'n_3'} + $kiso_nouryoku[3]) + (rand($lp) + 1)) + $kiso_hp;
		$ex=0;
		$lv=1;
		$gold=0;
		$n_0 = $kiso_nouryoku[0] + $in{'n_0'};
		$n_1 = $kiso_nouryoku[1] + $in{'n_1'};
		$n_2 = $kiso_nouryoku[2] + $in{'n_2'};
		$n_3 = $kiso_nouryoku[3] + $in{'n_3'};
		$n_4 = $kiso_nouryoku[4] + $in{'n_4'};
		$n_5 = $kiso_nouryoku[5] + $in{'n_5'};
		$n_6 = $kiso_nouryoku[6] + $in{'n_6'};
		$c_syoku = $in{'syoku'};
		$ksyoku = $c_syoku;
		$klv=1;
		&class;
		unshift(@new,"$in{'id'}<>$in{'pass'}<>$in{'site'}<>$in{'url'}<>$in{'c_name'}<>$in{'sex'}<>$in{'chara'}<>$n_0<>$n_1<>$n_2<>$n_3<>$n_4<>$n_5<>$n_6<>$c_syoku<>$kclass<>$hp<>$hp<>$ex<>$lv<>$gold<>$lp<>$total<>$kati<>$waza<><>0<>$sentou_limit<>$host<>$date<>\n");
	}

	open(OUT,">$chara_file");
	print OUT @new;
	close(OUT);

	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	if($in{'new'}) { &make_end; }
}
#------------------#
#  �N�b�L�[�̔��s  #
#------------------#
sub set_cookie {
	# �N�b�L�[��60���ԗL��
	$ENV{'TZ'} = "JST-9";
	($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time+5184000);

	@month=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	@week=('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$week[$wday],$mday,$month[$mon],$year+1900,$hour,$min,$sec);
	$cook="id<>$cookie_id\,pass<>$cookie_pass";
	print "Set-Cookie: FFADV=$cook; expires=$gmt\n";
}
#--------#
#  �]�E  #
#--------#
sub tensyoku {
	if($in{'syoku'} eq 'no') { &error("�E�Ƃ�I�����Ă��������B"); }
	$syoku = $in{'syoku'};
	$id = $in{'id'};

	&get_host;

	$date = time();

	# �t�@�C�����b�N
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(IN,"<$chara_file");
	@tensyoku = <IN>;
	close(IN);

	open(IN,"<$syoku_file");
	@syokudata = <IN>;
	close(IN);

	($a,$b,$c,$d,$e,$f,$g) = split(/<>/,$syokudata[$in{'syoku'}]);

	if(!$a) { $a = $kiso_nouryoku[0]; }
	if(!$b) { $b = $kiso_nouryoku[1]; }
	if(!$c) { $c = $kiso_nouryoku[2]; }
	if(!$d) { $d = $kiso_nouryoku[3]; }
	if(!$e) { $e = $kiso_nouryoku[4]; }
	if(!$f) { $f = $kiso_nouryoku[5]; }
	if(!$g) { $g = $kiso_nouryoku[6]; }

	$lv = 1;
	$ex = 0;

	@ten_new = ();
	foreach(@tensyoku) {
		($tid,$tpass,$tsite,$turl,$tname,$tsex,$tchara,$tn_0,$tn_1,$tn_2,$tn_3,$tn_4,$tn_5,$tn_6,$tsyoku,$tclass,$thp,$tmaxhp,$tex,$tlv,$tgold,$tlp,$ttotal,$tkati,$twaza,$ti_name,$ti_dmg,$tmons,$thost,$tdate) = split(/<>/);
		if($id eq $tid) {
			if ($tpass ne $in{'pass'}) { &error('�p�X���[�h���Ⴂ�܂��B'); }
			if($tn_0<$a||$tn_1<$b||$tn_2<$c||$tn_3<$d||$tn_4<$e||$tn_5<$f||$tn_6<$g){
				&error('�X�e�[�^�X���]�E�ɕK�v�Ȓl�ɒB���Ă��܂���');
			}
			$ksyoku=$tsyoku;
			$klv=1;
			&class;
			unshift(@ten_new,"$tid<>$tpass<>$tsite<>$turl<>$tname<>$tsex<>$tchara<>$a<>$b<>$c<>$d<>$e<>$f<>$g<>$syoku<>$kclass<>$thp<>$tmaxhp<>$ex<>$lv<>$tgold<>$tlp<>$ttotal<>$tkati<>$twaza<>$ti_name<>$ti_dmg<>$tmons<>$host<>$date<>\n");
		}else{
			push(@ten_new,"$_");
		}
	}

	open(OUT,">$chara_file");
	print OUT @ten_new;
	close(OUT);

	&read_winner;

	if($id eq $wid) {
		open(OUT,">$winner_file");
		print OUT "$wid<>$wpass<>$wsite<>$wurl<>$wname<>$wsex<>$wchara<>$a<>$b<>$c<>$d<>$e<>$f<>$g<>$syoku<>$kclass<>$wmaxhp<>$wmaxhp<>$ex<>$lv<>$wgold<>$wlp<>$wtotal<>$wkati<>$wwaza<>$wi_name<>$wi_dmg<>$wmons<>$host<>$date<>$wcount<>$lsite<>$lurl<>$lname<>\n";
		close(OUT);
	}

	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	&header;

	print <<"EOM";
<h1>�]�E���܂���</h1><hr size=0>
<p>
<form action="$script" method="get">
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="hidden" name=mode value=log_in>
<input type="submit" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}
#------------#
#  �̗͉�  #
#------------#
sub yado {
	&get_host;

	$date = time();

	# �t�@�C�����b�N
	if ($lockkey == 1) { &lock1; }
	elsif ($lockkey == 2) { &lock2; }

	open(IN,"<$chara_file");
	@YADO = <IN>;
	close(IN);

	$hit=0;@yado_new=();
	foreach(@YADO){
		($yid,$ypass,$ysite,$yurl,$yname,$ysex,$ychara,$yn_0,$yn_1,$yn_2,$yn_3,$yn_4,$yn_5,$yn_6,$ysyoku,$yclass,$yhp,$ymaxhp,$yex,$ylv,$ygold,$ylp,$ytotal,$ykati,$ywaza,$yi_name,$yi_dmg,$ymons,$yhost,$ydate) = split(/<>/);
		if($in{'id'} eq "$yid") {
			if ($ypass ne $in{'pass'}) { &error('�p�X���[�h���Ⴂ�܂��B'); }
			$yado_gold = $yado_dai * $ylv;
			if($ygold < $yado_gold) { &error("����������܂���"); }
			else { $ygold = $ygold - $yado_gold; }
			unshift(@yado_new,"$yid<>$ypass<>$ysite<>$yurl<>$yname<>$ysex<>$ychara<>$yn_0<>$yn_1<>$yn_2<>$yn_3<>$yn_4<>$yn_5<>$yn_6<>$ysyoku<>$yclass<>$ymaxhp<>$ymaxhp<>$yex<>$ylv<>$ygold<>$ylp<>$ytotal<>$ykati<>$ywaza<>$yi_name<>$yi_dmg<>$ymons<>$host<>$ydate<>\n");
		}else{
			push(@yado_new,"$_");
		}
	}

	open(OUT,">$chara_file");
	print OUT @yado_new;
	close(OUT);

	&read_winner;

	if($wid eq "$in{'id'}") {
		open(OUT,">$winner_file");
		print OUT "$wid<>$wpass<>$wsite<>$wurl<>$wname<>$wsex<>$wchara<>$wn_0<>$wn_1<>$wn_2<>$wn_3<>$wn_4<>$wn_5<>$wn_6<>$wsyoku<>$wclass<>$wmaxhp<>$wmaxhp<>$wex<>$wlv<>$wgold<>$wlp<>$wtotal<>$wkati<>$wwaza<>$wi_name<>$wi_dmg<>$wmons<>$host<>$ydate<>$wcount<>$lsite<>$lurl<>$lname<>\n";
		close(OUT);
	}

	# ���b�N����
	if(-e $lockfile) { unlink($lockfile); }

	&header;

	print <<"EOM";
<h1>�̗͂��񕜂��܂���</h1>
<hr size=0>
<form action="$script" method="get">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value="$in{'id'}">
<input type=hidden name=pass value="$in{'pass'}">
<input type=submit value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}
#------------------#
#  ���b�Z�[�W�폜  #
#------------------#
sub del_message{
	open(IN,"<$message_file");
	@MESSAGE = <IN>;
	close(IN);
	@mes_regist = ();
	$hit=0;
	foreach(@MESSAGE){
		($pid,$hid,$hname,$hmessage,$hhname,$htime) = split(/<>/);
		if($_[0] eq $pid || $_[0] eq $hid) { $hit=1; next; }
		push(@mes_regist,$_);
	}
	if(!$hit){return();}
	open(OUT,">$message_file");
	print OUT @mes_regist;
	close(OUT);
}
#----------------#
#  ���x���A�b�v  #
#----------------#
sub lv_up{
	$comment .= "$kname�́A���x�����オ�����I�I<p>";
	$uphp = int(rand($kn_3)) + 1;
	$kmaxhp = $kmaxhp + $uphp;
	$khp = $kmaxhp;
	$comment .= "HP��$uphp�オ�����B";
	$kex = 0;
	$klv += 1;
	if(int(rand(5)) == 0) { $kn_0 += 1; $t1 = 1;}
	if(int(rand(5)) == 0) { $kn_1 += 1; $t2 = 1;}
	if(int(rand(5)) == 0) { $kn_2 += 1; $t3 = 1;}
	if(int(rand(5)) == 0) { $kn_3 += 1; $t4 = 1;}
	if(int(rand(5)) == 0) { $kn_4 += 1; $t5 = 1;}
	if(int(rand(5)) == 0) { $kn_5 += 1; $t6 = 1;}
	if(int(rand(5)) == 0) { $kn_6 += 1; $t7 = 1;}
	if($t1) { $comment .= "�͂��オ�����B"; }
	if($t2) { $comment .= "�m�͂��オ�����B"; }
	if($t3) { $comment .= "�M�S���オ�����B"; }
	if($t4) { $comment .= "�����͂��オ�����B"; }
	if($t5) { $comment .= "��p�����オ�����B"; }
	if($t6) { $comment .= "�������オ�����B"; }
	if($t7) { $comment .= "���͂��オ�����B"; }
	&class;
}
#------------------#
#  �N���X��������  #
#------------------#
sub class{
	if($klv >= 42) {
		$class_lv = 6;
	}elsif($klv < 7){
		$class_lv = 0;
	}elsif($klv < 14){
		$class_lv = 1;
	}elsif($klv < 21){
		$class_lv = 2;
	}elsif($klv < 28){
		$class_lv = 3;
	}elsif($klv < 35){
		$class_lv = 4;
	}elsif($klv < 42){
		$class_lv = 5;
	}

	if($ksyoku == 0){
			$kclass = $FIGHTER[$class_lv];
	}elsif($ksyoku == 1){
			$kclass = $MAGE[$class_lv];
	}elsif($ksyoku == 2){
			$kclass = $PRIEST[$class_lv];
	}elsif($ksyoku == 3){
			$kclass = $THIEF[$class_lv];
	}elsif($ksyoku == 4){
			$kclass = $RANGER[$class_lv];
	}elsif($ksyoku == 5){
			$kclass = $ALCHEMIST[$class_lv];
	}elsif($ksyoku == 6){
			$kclass = $BARD[$class_lv];
	}elsif($ksyoku == 7){
			$kclass = $PSIONIC[$class_lv];
	}elsif($ksyoku == 8){
			$kclass = $VALKYRIE[$class_lv];
	}elsif($ksyoku == 9){
			$kclass = $BISHOP[$class_lv];
	}elsif($ksyoku == 10){
			$kclass = $LORD[$class_lv];
	}elsif($ksyoku == 11){
			$kclass = $SAMURAI[$class_lv];
	}elsif($ksyoku == 12){
			$kclass = $MONK[$class_lv];
	}elsif($ksyoku == 13){
			$kclass = $NINJA[$class_lv];
	}
}
#------------------#
# �������̃`�F�b�N #
#------------------#
sub max_strings(){
	if(length($in{'c_name'}) > $name_maxs){
		&error("���O�͔��p$name_maxs�����ȓ��ŋL�����Ă�������");
	}elsif(length($in{'site'}) > $site_maxs){
		&error("�z�[���y�[�W���͔��p$site_maxs�����ȓ��ŋL�����Ă�������");
	}elsif(length($in{'url'}) > $url_maxs){
		&error("�z�[���y�[�W�͂t�q�k�͔��p$�����ȓ��ŋL�����Ă�������");
	}elsif(length($in{'waza'}) > $waza_maxs){
		&error("�Z�������R�����g�͔��p$waza_maxs�����ȓ��ŋL�����Ă�������");
	}elsif(length($in{'mes'}) > $mes_maxs){
		&error("���b�Z�[�W�͔��p$mes_maxs�����ȓ��ŋL�����Ă�������");
	}
}
