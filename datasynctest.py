# encoding: utf-8

import os
from string import Template
import re


def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).upper()


def gen_test():
    name_list = ['ContactInfoSyncService', 'KtggSyncService', 'LegalAdjudicativeDocumentsSyncService',
                 'LegalCourtNoticeSyncService', 'LegalDishonestPersonsSubjectToEnforcementSyncService',
                 'LegalPersonsSubjectToEnforcementSyncService', 'ManageBidwinningSyncService',
                 'ManageRecruitSyncService', 'ManageTenderSyncService', 'OtherEastmoneyPledgeSyncService',
                 'PropDomainWebsiteSyncService', 'QualHightechSyncService', 'QyxgChinaVentureSyncService',
                 'QyxxAnnualReportDbxxSyncService', 'QyxxAnnualReportSbxxSyncService', 'QyxxBasicSyncService',
                 'QyxxBaxxSyncService', 'QyxxBgxxMergeSyncService', 'QyxxEntinvSyncService', 'QyxxFrinvSyncService',
                 'QyxxFzjgCleanSyncService', 'QyxxGdxxSyncService', 'QyxxJqkaCwzbXjllSyncService',
                 'QyxxJqkaCwzbZcfzSyncService', 'QyxxJqkaCwzbZhsySyncService', 'QyxxJqkaCwzbZhzbSyncService',
                 'QyxxJqkaIpoBasicSyncService', 'QyxxJyycSyncService', 'QyxxKcbCwzbXjllSyncService',
                 'QyxxKcbCwzbZhsySyncService', 'QyxxKcbCwzbZhzbSyncService', 'QyxxKcbIpoBasicSyncService',
                 'QyxxMordetailSyncService', 'QyxxSharesimpawnSyncService', 'QyxxWanfangZhuanliSyncService',
                 'QyxxXzcfSyncService', 'RiskTaxIllegalSyncService', 'RjzzqSyncService', 'TddySyncService',
                 'XgxxShangbiaoSyncService', 'ZpzzqSyncService']

    test_code_temp = Template('''
    @Resource(name = BeanConstnts.${case_name})
    private IDataSyncService ${raw_name_low}Impl;
    
    @Test
    public void test${raw_name}(){
        /*
         * 数据同步
         */
        CompanyManager companyManager = new CompanyManager();
        
        companyManager.setCompanyName("君航信通(北京)信息技术有限公司");
        companyManager.setQyxxId("2c637b02298b43c5906ab1d91425e734");
        
        // 同步数据参数
        TaskGenAndDataSyncDTO taskGenAndDataSyncDTO = new TaskGenAndDataSyncDTO();
        taskGenAndDataSyncDTO.setCompanyName("君航信通(北京)信息技术有限公司");// 企业名称
        taskGenAndDataSyncDTO.setCompanyId("2c637b02298b43c5906ab1d91425e734");// 企业id
        taskGenAndDataSyncDTO.setCompanyManager(companyManager);// companyManager
        taskGenAndDataSyncDTO.setVersion(DateUtil.format(new Date(), "yyyyMMdd") + "0001");
        taskGenAndDataSyncDTO.setPage(new Page(1,20));
        taskGenAndDataSyncDTO.setSyncPageDataAllFlag(true);//
        ${raw_name_low}Impl.sync(taskGenAndDataSyncDTO);
    }
    ''')
    for name in name_list:
        if name == 'QyxxBasicSyncService':
            continue
        raw_name = name
        case_name = get_lower_case_name(name)
        raw_name_low = raw_name[0].lower() + raw_name[1:]
        print(test_code_temp.substitute(case_name=case_name, raw_name=raw_name, raw_name_low=raw_name_low))
        # break
    pass


if __name__ == '__main__':
    gen_test()

    pass
