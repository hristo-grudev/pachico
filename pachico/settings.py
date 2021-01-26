BOT_NAME = 'pachico'

SPIDER_MODULES = ['pachico.spiders']
NEWSPIDER_MODULE = 'pachico.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'pachico.pipelines.PachicoPipeline': 100,

}