from trading_monitor import TradingMonitor
import logging
import time
import sys
import os

class HeadlessMonitor(TradingMonitor):
    def __init__(self):
        # إعداد تسجيل مخصص لـ Render
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)]
        )
        
        # استدعاء المُنشئ الأب مع الوسيط الصحيح
        super().__init__(is_headless=True)
        
        # بدء المراقبة
        self.start_monitoring()
        
        # الحفاظ على البرنامج قيد التشغيل
        try:
            while self.is_running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_monitoring()
            sys.exit(0)
        
    def log_message(self, message, level="info"):
        """تسجيل الرسائل فقط في ملف السجل"""
        # إرسال الرسائل إلى stdout (مهم لـ Render)
        if level.lower() == "error":
            logging.error(message)
        elif level.lower() == "warning":
            logging.warning(message)
        else:
            logging.info(message)

if __name__ == "__main__":
    # تحقق من المتغيرات البيئية الأساسية
    required_env_vars = ['COINEX_ACCESS_ID', 'COINEX_SECRET_KEY']
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        logging.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)
    
    bot = HeadlessMonitor()
