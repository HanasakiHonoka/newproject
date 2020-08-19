# encoding: utf-8

import os
from string import Template
import re


def isNum(char):
    return ("" + char).isnumeric()


def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if (char.isupper() or ("" + char).isnumeric()) and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


def task_gen_service():
    dir_path = '''D:\\WorkSpace\\serviceplatform-microservice-datacenter\\biz\\src\\main\\java\\cn\\com\\beijingipo\\datacenter\\biz\\taskgen\\service\\impl\\'''
    list = os.listdir(dir_path)
    for raw_name in list:
        name = raw_name.split(".")[0]
        if name == 'AbstractTaskGenServiceImpl' or name == 'CompanyManagerServiceImpl':
            continue
        name = name.replace('Impl', '')
        bean_name = get_lower_case_name(name)
        const_temp = Template('''public static final String ${bean_name} = "${name}";''')
        print(const_temp.substitute(bean_name=bean_name, name=name))


def task_gen_service_modify():
    dir_path = '''e:\\cache'''
    list = os.listdir(dir_path)
    for file_name in list:
        with open(dir_path + "\\" + file_name, "r", encoding="utf8") as f1, open("./res/" + file_name, 'w',
                                                                                 encoding="utf8") as f2:
            for line in f1.readlines():
                if re.match('@Service\(".*?"\)', line):
                    name = get_lower_case_name(file_name.split(".")[0].replace('Impl', ''))
                    f2.write('@Service(BeanConstnts.' + name + ')\n')
                    pass
                else:
                    f2.write(line)
            pass
        # break
    pass


def datasync():
    dir_path = '''e:/cache/datasync/'''
    list = os.listdir(dir_path)
    name_list = []
    for raw_name in list:
        name = raw_name.replace('Impl.java', '')
        name_list.append(name)
        # bean_name = get_lower_case_name(name)
        # const_temp = Template('''public static final String ${bean_name} = "${name}";''')
        # print(const_temp.substitute(bean_name=bean_name, name=name))
    print(name_list)
    print(len(name_list))
    pass


def datasync_modify():
    dir_path = '''e:/cache/datasync/'''
    list = os.listdir(dir_path)
    for file_name in list:
        with open(dir_path + file_name, "r", encoding="utf8") as f1, open("./res2/" + file_name, 'w',
                                                                          encoding="utf8") as f2:
            for line in f1.readlines():
                if re.match('@Service\(".*"\)', line):
                    name = get_lower_case_name(file_name.split(".")[0].replace('Impl', ''))
                    f2.write('@Service(BeanConstnts.' + name + ')\n')
                elif re.match('@Resource\(.*\)', line.replace(' ', '')):
                    print(line)
                    name = get_lower_case_name(
                        file_name.replace('SyncServiceImpl.java', '') + 'TianyanchaTaskGenService')
                    f2.write('@Resource(name = BeanConstnts.' + name + ')\n')
                else:
                    f2.write(line)
            pass
        # break
    pass


def int_check():
    quanxian = '''
    搜索接口 816 
企业简介 755 
企业基本信息 818 
主要人员 820 
股东信息 821 
对外投资 823 
分支机构 824 
变更记录 822 
企业年报 825 
香港公司、社会组织、律所 459 
法律诉讼 842 
法院公告 841 
开庭公告 840 
失信人 843 
被执行人 839 
司法协助 756 
知识产权出质 795 
公告催告 796 
经营异常 848 
行政处罚 847 
行政处罚-信用中国 852 
严重违法 846 
股权出质 845 
动产抵押 844 
欠税公告 851 
司法拍卖 850 
清算信息 849 
土地抵押 955 
税收违法 957 
环保处罚 959 
商标信息 838 
专利 837 
作品著作权 833 
著作权 836 
网站备案 835 
融资历史 826 
核心团队 827 
企业业务 828 
投资事件 829 
竞品信息 830 
招聘 879 
招投标 887 
税务评级 884 
产品信息 882 
资质证书 880 
微信公众号 834 
进出口信用 881 
行政许可 888 
行政许可-信用中国 889 
抽查检查 883 
新闻 943 
上市公告 857 
股票行情 853 
企业简介 854 
高管信息 855 
参股控股 856 
十大股东和十大流通股东 859 
利润表 971 
资产负债表 972 
现金流量表 973 
财务简析 798 
获取人简介 448 
人所有角色 449 
人所有公司 450 
人所有合作伙伴 451 
企业图谱 783 
股权结构图 453 
投资族谱 455 
最终受益人 746 
实际控制权 747 
历史工商信息 878 
历史股东信息 877 
历史对外投资 876 
历史法律诉讼 874 
历史开庭公告 875 
历史法院公告 873 
历史失信人 872 
历史被执行人 871 
历史经营异常 996 
历史行政处罚 870 
历史动产抵押 866 
历史股权出质 868 
历史行政许可 867 
历史行政许可-信用中国 869 
历史网站备案 995 
    '''
    strr = '123'
    xianyou = '''
    ABONRMALHISTORY_INFO(996,"abnormalhistoryInfo"),
    ABNORMAL_INFO(848,"abnormalInfo"),
    ALLCOMPANYS_INFO(450,"allcompanysInfo"),
    ANNOUNCEMENTHISTORY_INFO(875,"announcementhistoryInfo"),
    ANNOUNCEMENT_INFO(857,"announcementInfo"),
    ANNUALREPORT_INFO(825,"annualreportInfo"),
    APPBK_INFO(882,"appbkInfo"),
    BALANCESHEET_INFO(972,"balancesheetInfo"),
    BASIC_INFO(818,"basicInfo"),
    BIDS_INFO(887,"bidsInfo"),
    BRANCHR_INFO(824,"branchInfo"),
    CASHFLOW_INFO(973,"cashflowInfo"),
    CERTIFICATE_INFO(880,"certificateInfo"),
    CHANGE_INFO(822,"changeInfo"),
    CHECK_INFO(883,"checkInfo"),
    C_INFO(783,"cInfo"),
    COMPANYHOLDING_INFO(747,"companyholdingInfo"),
    COMPANY_INFO(854,"companyInfo"),
    COPYREG_INFO(836,"copyregInfo"),
    COPYREGWORKS_INFO(833,"copyregworksInfo"),
    COURTANNOUNCEMENT_INFO(841,"courtannouncementInfo"),
    COURT_INFO(873,"courtInfo"),
    CREDITCHINAHISTORY_INFO(869,"creditchinahistoryInfo"),
    CREDITCHINA_INFO(852,"creditchinaInfo"),
    DESCRIPTION_INFO(448,"descriptionInfo"),
    DISHONESTHISTORY_INFO(872,"dishonesthistoryInfo"),
    DISHONEST_INFO(843,"dishonestInfo"),
    EMPLOYMENTS_INFO(879,"employmentsInfo"),
    ENVIRONMENTALPENALTY_INFO(959,"environmentalpenaltyInfo"),
    EQUITYHISORY_INFO(868,"equityhistoryInfo"),
    EQUITY_INFO(845,"equityInfo"),
    EQUITYRATIO_INFO(453,"equityratioInfo"),
    FINANCIALANALYSIS_INFO(798,"financialanalysisInfo"),
    FINDHITORYRONGZI_INFO(826,"findhistoryrongziInfo"),
    FINDJINGPIN_INFO(830,"findjingpinInfo"),
    FINDTEAMMEMBER_INFO(827,"findteammemberInfo"),
    FINDZANLI_INFO(829,"findtzanliInfo"),
    FROFILE_INFO(755,"frofileInfo"),
    INTRODUCTION_INFO_SERVICE(755,"introductionInfoService"), //兩個都是755
    GETLICENSECREDITCHINA_INFO(889,"getlicensecreditchinaInfo"),
    GETLICENSE_INFO(888,"getlicenseInfo"),
    GETPLEDGEREG_INFO(795,"getpledgeregInfo"),
    GETPRIDUCT_INFO(828,"getproductInfo"),
    HOLDERHISTORY_INFO(877,"holderhistoryInfo"),
    HOLDER_INFO(821,"holderInfo"),
    HOLDINGCOMPANY_INFO(856,"holdingcompanyInfo"),
    HUMANHOLDING_INFO(746,"humanholdingInfo"),
    IC_INFO(878,"icInfo"),
    ICPHISTORY_INFO(995,"icphistoryInfo"),
    ICP_INFO(835,"icpInfo"),
    ILLEGAL_INFO(846,"illegalInfo"),
    IMPORTANDEXPORY_INFO(881,"importandexportInfo"),
    INVERST_INFO(823,"inverstInfo"),
    INVEST_INFO(876,"investInfo"),
    INVESTTREE_INFO(455,"investtreeInfo"),
    JUDICIAL_INFO(756,"judicialInfo"),
    JUDICIALSALE_INFO(850,"judicialsaleInfo"),
    KTANNOUNCEMENT_INFO(840,"ktannouncementInfo"),
    LANDMORTGAGE_INFO(955,"landmortgageInfo"),
    LAWSUITHISTORY_INFO(874,"lawsuithistoryInfo"),
    LAWSUIT_INFO(842,"lawsuitInfo"),
    LICENSE_INFO(867,"licenseInfo"),
    LIQUIDATING_INFO(849,"liquidatingInfo"),
    MORTGAGEHISTORY_INFO(866,"mortgagehistoryInfo"),
    MORTGAGE_INFO(844,"mortgageInfo"),
    NEWS_INFO(943,"newsInfo"),
    OWNTAX_INFO(851,"owntaxInfo"),
    PARTNERS_INFO(451,"partnersInfo"),
    PATENTS_INFO(837,"patentsInfo"),
    PROFIT_INFO(971,"profitInfo"),
    PUBLICNOTICE_INFO(796,"publicnoticeInfo"),
    PUBLICWECHAT_INFO(834,"publicwechatInfo"),
    PUNISHMENTHISTORY_INFO(870,"punishmenthistoryInfo"),
    PUNISHMENT_INFO(847,"punishmentInfo"),
    ROLES_INFO(449,"rolesInfo"),
    SEARCH_INFO(816,"searchInfo"),
    SENIOREXECUTIVE_INFO(855,"seniorexecutiveInfo"),
    SHAREHOLDER_INFO(859,"shareholderInfo"),
    STAFF_INFO(820,"staffInfo"),
    TAXCONTRAVENTION_INFO(957,"taxcontraventionInfo"),
    TAXCREDIT_INFO(884,"taxcreditInfo"),
    TM_INFO(838,"getTmInfo"),
    VOLATILITY_INFO(853,"volatilityInfo"),
    XGBASE_INFO(459,"xgbaseInfo"),
    ZHIXINGHISTORY_INFO(871,"zhixinghistoryInfo"),
    ZHIXINNG_INFO(839,"zhixingInfo"),

    DETAILS_LAND_MORTAGAGE_INFO(956,"detailsLandMortagageInfo"),
    SHAREHOLDERS_PLEDGE_INFO(1019,"shareholdersPledgeInfo"),
    INDICATORS_YEAR_INFO(967,"indicatorsYearInfo"),
    INDICATORS_QUARTERLY_INFO(968,"indicatorsQuarterlyInfo"),
    RISK_TAX_ILLEGAL_DETAIL(958,"riskTaxIllegalDetail")
    ;

   
    '''
    quanxian_num = re.findall(r"\d*", quanxian)
    while '' in quanxian_num:
        quanxian_num.remove('')
    xianyou_num = re.findall(r"\d*", xianyou)
    while '' in xianyou_num:
        xianyou_num.remove('')
    print(len(quanxian_num))
    print(len(xianyou_num))
    for num in xianyou_num:
        if num not in quanxian_num:
            print(num)


def movie_name_fix():
    raw_name = '''
private Integer director1Id;

    private String director1Name;

    private Integer director1Amount;

    private Float director1Boxoffice;

    private Integer director2Id;

    private String director2Name;

    private Integer director2Amount;

    private Float director2Boxoffice;

    private Integer scenarist1Id;

    private String scenarist1Name;

    private Integer scenarist1Amount;

    private Float scenarist1Boxoffice;

    private Integer scenarist2Id;

    private String scenarist2Name;

    private Integer scenarist2Amount;

    private Float scenarist2Boxoffice;

    private Integer actor1Id;

    private String actor1Name;

    private Integer actor1Amount;

    private Float actor1Boxoffice;

    private Integer actor2Id;

    private String actor2Name;

    private Integer actor2Amount;

    private Float actor2Boxoffice;
'''
    name_list = raw_name.split(";")
    name_list = [x.strip() for x in name_list]
    sum = 0
    for name in name_list:
        if name == '':
            continue
        lname = name.split(' ')[2]
        gname = get_lower_case_name(lname)
        print('@TableField("%s")' % gname)
        print(name + ';\n')
        sum = sum + 1
        # break
    print(sum)
    pass


if __name__ == '__main__':
    # int_check()
    movie_name_fix()
    pass
