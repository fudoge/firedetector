package com.example.fire_detector

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.example.fire_detector.ui.navigation.AppNavHost
import com.example.fire_detector.ui.theme.Fire_detectorTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            Fire_detectorTheme {
                AppNavHost()
            }
        }
    }
}