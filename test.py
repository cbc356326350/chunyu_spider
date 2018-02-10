aa = ['\n\t\t', '简介 :', '\n\t\t黑龙江省第三医院(黑龙江省神经精神病防治院)建于1953年，是由当时的中国人民解放军34、35、36后方医院合并而成，当时称战勤医院，后改称黑龙江省神经精神病防治院，隶属于黑龙江省卫生厅，属非营利性全民事业单位，是，医院临床科室有精神科、精神外科、神经内科、神经外科、神经康复科、普通内科、普通外科、循环内科、妇产科、骨科、介入治疗科、皮肤科、急诊科等科室。临床辅助科室有电诊科、理疗科、病理科、检验科、放射科、CT磁共振室、血液净化中心、生物反技术指导、社区服务网点建设和精神科卫生技术人员培训等项工作。设有司法精神医学鉴定小组负责伊春市、黑河地区和大兴安岭地区的司法精神医学鉴定工作。 ', '\r', '\u3000\u3000黑龙江省第三医院占地面积50000平方米，医疗用房36800平方米，设施先系统、生物反馈治疗仪和常规特殊化检验系统，医疗设备配置合理。 ', '\r', '\u3000\u3000黑龙江省第三医院有一批享誉省内外的医学专家和一大批学识渊博，临床经验丰富的中青年业务骨干，在医院现有的卫生专业技术人员中，正高职16人，副高职56人，具有人员素质好，机动性强，反应速度快，辐射面广，救治成功率高的特点。 ', '\r', '\u3000\u3000经过五十年的建设发展，黑龙江省第三医院已成为黑龙江省北部地区集医疗、预防、科研、教学、社区服务为一体，具有医疗资源雄厚，人才优势、技术优势000年至2003年分别通过黑龙江省“公众信誉”的医院和省内“医德医风”省内最佳医院评审达标合格医院。 ', '\r', '\u3000\u3000医院长期担任黑龙江省医学会精神科专业委员会副主任委员，神经科专业委员会委员，国家精神疾病康复专业委员会理事，黑龙江省脑立体定向手术治疗癫痫和精神障碍荣获黑龙江省政府科技成果奖之后，医院在高血压脑病、脑出血脑梗塞，脑瘤和循环系统常见病和疑难病、临床医疗、科研等方面取得了成果。随着精神卫生科学研究的深入，医院在精神疾病的预防和临床治疗方面形成一整套术的进步与发展。\n\t']
def item_is_not_empty(c):
    return c and c.strip()


def filter_empty(c):
    return list(filter(item_is_not_empty, c))

des = filter_empty(aa)
des = list(map(lambda a: a.strip(), des))
print(des)