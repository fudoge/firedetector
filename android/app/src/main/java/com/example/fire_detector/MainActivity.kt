package com.example.fire_detector

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.example.fire_detector.ui.setup.UrlSetupScreen
import com.example.fire_detector.ui.theme.Fire_detectorTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Fire_detectorTheme {
                UrlSetupScreen(
                    onConnectClick = { url ->
                        println("입력된 URL: $url")
                    }
                )
            }
        }    }
}