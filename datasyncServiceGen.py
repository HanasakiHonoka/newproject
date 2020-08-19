# encoding: utf-8

from string import Template
synctemp = Template('''
package cn.com.beijingipo.datacenter.biz.datasync.service.impl;

import cn.com.beijingipo.datacenter.biz.datasync.qylist.entity.CompanyManager;
import cn.com.beijingipo.datacenter.biz.datasync.qylist.entity.${hump_name_U};
import cn.com.beijingipo.datacenter.biz.datasync.qylist.service.I${hump_name_U}Service;
import cn.com.beijingipo.datacenter.biz.taskgen.service.ITaskGenService;
import com.alibaba.fastjson.JSONObject;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

@Slf4j
@Service("${hump_name_U}SyncService")
public class ${hump_name_U}SyncServiceImpl extends DataSyncServiceImpl {

    @Autowired
    private I${hump_name_U}Service ${hump_name}Service;

    @Resource(name = "${hump_name_U}TaskGenService")
    private ITaskGenService ${hump_name_U}TaskGenService;

    /**
     * json转换成表对应实体
     * @param jsonObject
     * @return
     */
    private ${hump_name_U} jsonConverter(JSONObject jsonObject) {
        ${hump_name_U} ${hump_name} = jsonObject.toJavaObject(${hump_name_U}.class);
        //List<ContactInfo> contactInfoList = JSON.parseArray(jsonObject.toJSONString(), ContactInfo.class);
        return ${hump_name};
    }

    @Override
    public JSONObject getDataFromTrddata(CompanyManager companyManager, String companyId) {
        return ${hump_name_U}TaskGenService.gen(companyManager, companyId);
    }

    @Override
    public void mysqlSync(JSONObject entityData) {
        ${hump_name_U} ${hump_name} = this.jsonConverter(entityData);
        //向mysql查询是否有该公司的相关信息
        QueryWrapper<${hump_name_U}> wrapper = new QueryWrapper<>();
        wrapper.eq(${hump_name_U}.BBD_QYXX_ID, ${hump_name}.getBbdQyxxId());
        ${hump_name_U} ${hump_name}InDB = ${hump_name}Service.getOne(wrapper);

        if(${hump_name}InDB == null) {
            //如果没有就保存
            ${hump_name}Service.save(${hump_name});
        } else {
            //有就更新
            log.info(this.getClass().getName() + "需要更新");
            //UpdateWrapper<ContactInfo> updateWrapper = new UpdateWrapper<>();
            //iContactInfoService.update(contactInfo, updateWrapper);
        }
    }
}
''')

taskgentemp = Template(
'''
package cn.com.beijingipo.datacenter.biz.taskgen.service.impl;

import cn.com.beijingipo.datacenter.biz.datasync.qylist.entity.CompanyManager;
import cn.com.beijingipo.trddata.facade.constant.request.TrdDataProviderEnum;
import cn.com.beijingipo.trddata.facade.dto.request.TrdDataRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Slf4j
@Service("${hump_name_U}TaskGenService")
public class ${hump_name_U}TaskGenServiceImpl extends TaskGenServiceImpl{

    private static String ${name_U}_DATA_SYNC_TASK_ID = "";

    @Override
    public String getTaskId() {
        return ${name_U}_DATA_SYNC_TASK_ID;
    }

    @Override
    public TrdDataRequest setRequest(CompanyManager companyManager) {
        if (this.getProvider() == TrdDataProviderEnum.TIANYANCHA) {
            //TianyanchaDataBasicInfoRequest request = new TianyanchaDataBasicInfoRequest();
            //request.setName(companyManager.getCompanyName());
            //return request;
        } else if (this.getProvider() == TrdDataProviderEnum.QUANTOM_DATA) {
            //...
        }
        return null;
    }
}
'''
)
# ,,
table_list=['qyxx_basic','contact_info','qyxx_gdxx','qyxx_baxx','qyxx_bgxx_merge','qyxx_fzjg_clean','qyxx_frinv','qyxx_entinv','qyxx_annual_report_dbxx','qyxx_annual_report_sbxx','qyxx_jqka_ipo_basic','qyxx_jqka_cwzb_zhzb','qyxx_jqka_cwzb_xjll','qyxx_jqka_cwzb_zhsy','qyxx_sharesimpawn','qyxx_mordetail','tddy','rjzzq','zpzzq','xgxx_shangbiao','prop_domain_website','qual_hightech','legal_adjudicative_documents','legal_court_notice','ktgg','qyxx_xzcf','manage_tender','manage_bidwinning','qyxx_wanfang_zhuanli','qyxx_jyyc','manage_recruit','qyxg_china_venture','risk_tax_illegal','legal_dishonest_persons_subject_to_enforcement','legal_persons_subject_to_enforcement','other_eastmoney_pledge','qyxx_kcb_cwzb_xjll','qyxx_jqka_cwzb_zcfz','qyxx_kcb_cwzb_zhsy','qyxx_kcb_cwzb_zhzb','qyxx_kcb_ipo_basic']
temp_test = Template('''
name=${name}is
''')
def str2Hump(text):
    arr = filter(None, text.lower().split('_'))
    res = ''
    j = 0
    for i in arr:
        if j == 0:
            res = i
        else:
            res = res + i[0].upper() + i[1:]
        j += 1
    return res

def str2HumpU(text):
    arr = filter(None, text.lower().split('_'))
    res = ''
    j = 0
    for i in arr:
        res = res + i[0].upper() + i[1:]
        j += 1
    return res


def gen(table_name):
    pass


temp_sql = Template('''
update company_analysis ca set ${raw_name}_num = (select count(1) from ${raw_name} qgd where ca.bbd_qyxx_id = qgd.bbd_qyxx_id);
''')

if __name__ == '__main__':

    with open("sql.sql","w") as f:
        for table_name in table_list:
            f.write(temp_sql.substitute(raw_name=table_name))
    # print(taskgentemp.substitute(hump_name_U=table_hump_name_U, hump_name=table_hump_name, name_U=table_name_U))
    pass
