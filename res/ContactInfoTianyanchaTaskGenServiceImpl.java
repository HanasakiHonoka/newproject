package cn.com.beijingipo.datacenter.biz.taskgen.service.impl;

import cn.com.beijingipo.datacenter.biz.datasync.qylist.entity.CompanyManager;
import cn.com.beijingipo.trddata.facade.constant.request.TrdDataApiEnum;
import cn.com.beijingipo.trddata.facade.constant.request.TrdDataProviderEnum;
import cn.com.beijingipo.trddata.facade.dto.request.TrdDataRequest;
import cn.com.beijingipo.trddata.facade.dto.request.tianyancha.TianyanchaDataBasicInfoRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Slf4j
@Service(BeanConstnts.CONTACT_INFO_TIANYANCHA_TASK_GEN_SERVICE)
public class ContactInfoTianyanchaTaskGenServiceImpl extends AbstractTaskGenServiceImpl {

    @Override
    public TrdDataApiEnum getApi() {
        return TrdDataApiEnum.BASIC_INFO;
    }

    @Override
    public TrdDataProviderEnum getProvider() {
        return TrdDataProviderEnum.TIANYANCHA;
    }

    @Override
    public TrdDataRequest setRequest(CompanyManager companyManager) {
        TianyanchaDataBasicInfoRequest request = new TianyanchaDataBasicInfoRequest();
        request.setName(companyManager.getCompanyName());
        return request;
    }

}
